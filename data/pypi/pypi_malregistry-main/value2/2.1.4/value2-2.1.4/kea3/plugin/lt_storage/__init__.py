"""
long term storage - store & retrieve files

setup:
    +--------+                            +----------+
    | CLIENT |   upload: rsync over ssh   |  SERVER  |
    | store  |  ------------------------> |- sshd    |
    |        |     check status: REST     |          |
    | check  | <------------------------  |- bottle  |
    |        |      download: http(s)     |          |
    | get    | <------------------------  |- web srv |
    +--------+                            +----------+    
"""

from datetime import datetime
from functools import partial
import logging
import os
import tempfile
import time

import humanfriendly as hf
import fantail

from kea3 import kmeta, util, models

lg = logging.getLogger(__name__)

def _get_store(app, args):
    lts_conf = app.conf['plugin']['lt_storage']
    if args.store:
        store = lts_conf['stores'][args.store]
        lg.info("using store %s", args.store)
    elif 'default_store' in lts_conf:
        defstore = lts_conf['default_store']
        lg.info("using store %s", defstore)
        store = lts_conf['stores'][defstore]
        app.conf['plugin']['lt_storage']['stores'][args.store]
    else:
        lg.warning("please specify store: %s", " ".join(list(lts_conf['stores'].keys())))
        return
    return store


@fantail.subparser
def lts(app, args):
    """Long term storage - rsync data to ssh backup hosts"""
    pass


@fantail.arg('-s', '--store')
@fantail.arg("targetfile", help="save as", nargs='?')
@fantail.arg("short", help='short checksum')
@fantail.subcommand(lts, 'get')
def fs_download(app, args):
    khash = kmeta.find_khash(app, short=args.short)
    rsync = app.conf['plugin']['lt_storage']['rsync_get']
    if args.targetfile:
        targetfile = args.targetfile
    else:
        targetfile = khash['basename']

    app.message("saving to {}".format(targetfile))
    if os.path.exists(targetfile):
        target_khash = kmeta.get_kfile(app, targetfile).khash
        if target_khash == khash:
            app.message("File is already downloaded")
            return
        else:
            app.error("Target file exists & differs - please (re)move first")
            return
        
    for xlink in khash['xlink']:
        cl = rsync + ' {} {}'.format(xlink, targetfile)
        os.system(cl)
        break

@fantail.arg('-s', '--store')
@fantail.arg("filename")
@fantail.subcommand(lts, 'store')
def fs_upload(app, args):
    filename = args.filename
    kfile = kmeta.get_kfile(app, filename)
    sha256 = kfile.khash.sha256
    
    store = _get_store(app, args)
    if store is None:
        return
        
    host = store['host']
    path = store['path']
    rsync = app.conf['plugin']['lt_storage']['rsync_store']
    targetpath = path +  '/{}/{}'.format(sha256[:3], sha256)
    targetfile = targetpath + '/file'
    
    cl =  rsync + ' --rsync-path="mkdir -p {}; rsync" {} {}:{}'.format(targetpath, filename, host, targetfile)
    print("start file rsync")
    print(cl)
    os.system(cl)

    xlink = '{}:{}'.format(host, targetfile)
    kfile.set('xlink', xlink)
    
    print('store file metadata')
    metaname = 'meta.{}.gml'.format(datetime.now().strftime('%Y%m%d%H%M%S'))
    metafile = '/tmp/{}'.format(metaname)
    app.api.dump_to_file(app, filename, metafile)
    
    metatargetfile = targetpath + '/' + metaname
    cl =  rsync + ' {} {}:{}'.format(metafile, host, metatargetfile)
    print("start metadata rsync")
    print(cl)
    os.system(cl)
    os.unlink(metafile)
    print("finished rsync for", kfile.khash.short)


@fantail.arg('-l', '--ltsstore')
@fantail.subcommand(lts, 'host')
def fs_host(app, args):
    
    from bottle import Bottle, run
    from bottle import jinja2_view, route
    from bottle import static_file
    
    if args.ltsstore:
        lts_store = app.conf['plugin']['lt_storage']['stores'][args.ltsstore]
        lts_path = lts_store['path']
        assert os.path.exists(lts_path)
    else:
        lts_path = None

    def get_lts_path(khash):
        s256 = khash.sha256
        if lts_path is None:
            rv = None
        rv = '{}/{}/{}/file'.format(lts_path, s256[:3], s256)
        print(rv)
        if not os.path.exists(rv):
            rv = None
        print(khash.short, lts_path, rv)
        return rv
    
    template_folder = os.path.join(os.path.dirname(__file__), 'templates')
    j2view = partial(jinja2_view,  template_lookup=[template_folder])

    bottle_app = Bottle()
    
    @bottle_app.route('/')
    @j2view('index.html')
    def index():
        raw_timestamp, stats = app.api.get_stats(app)
        stat_timestamp = datetime.fromtimestamp(raw_timestamp)
        timediff = hf.format_timespan(time.time() - float(raw_timestamp), max_units=1)
        stat_timestamp = stat_timestamp.strftime('%d %B %Y %H:%M:%S')
        stat_timestamp = f"{stat_timestamp} ({timediff} ago)"

        return dict(title='Kea3!',
                    stat_timestamp = stat_timestamp,
                    stats = stats,
                    current_item='Home')

    @bottle_app.route('/download/<checksum>')
    def download(checksum):
        khash = kmeta.find_khash(app, short=checksum)
        basename = khash['basename']
        lts_path = get_lts_path(khash)
        return static_file('file', root=os.path.dirname(lts_path), download=basename)

    
    @bottle_app.route('/checksum/<checksum:path>')
    @bottle_app.route('/checksum')
    @j2view('checksum.html')
    def checksum(checksum=None):
        data = dict(current_item='Checksum')
        if checksum is None:
            data['title'] = "Please enter a checksum"
            return data
        
        khash = kmeta.find_khash(app, short=checksum)
        if khash is None:
            data['title'] = "Please enter a valid checksum"
            return data

        data['in_this_lts'] = get_lts_path(khash) is not None
        
        data['khash'] = khash
        data['keyvals'] = list(kmeta.get_keyvals(app, khash, formatted=False))
        data['title'] = "Checksum: {}".format(checksum)
        
        return data                    

    @bottle_app.route('/project/<project>/<offset:int>')
    @bottle_app.route('/project/<project>')
    @bottle_app.route('/project')
    @j2view('project.html')
    def project(project = None, offset=0):
        session = app.db_session

        from kea3.models import KkeyVal, KHash, KFile
        from sqlalchemy import distinct, func
        from sqlalchemy.orm import aliased
        
        data = dict(current_item='Project', project=project, offset=offset)
        
        if project is None:
            data['title'] = 'Project List'
            data['project_list'] = session.query(KkeyVal.val, func.count(KkeyVal.khash_id))\
                                          .filter(KkeyVal.key == 'project')\
                                          .group_by(KkeyVal.val)\
                                          .all()
            
        else:
            kkbn = aliased(KkeyVal)
            data['title'] = 'Project: {}'.format(project)
            khash_list = session.query(KHash, KkeyVal, kkbn, KFile)\
                .join(KHash.keyvals).join(KHash.files).join(kkbn, KHash.keyvals)\
                .filter(kkbn.key == 'basename')\
                .filter(KkeyVal.key == 'project')\
                .filter(KkeyVal.val == project)\
                .order_by(KFile.mtime.desc())\
                .offset(offset)\
                .limit(20).all()
            
            data['khash_list'] = khash_list
            
        return data

    run(bottle_app, host='localhost', port=7778, debug=True, reloader=True)
