import requests
import random
import subprocess
import shutil
import os
import tempfile
import tarfile
import csv
import zipfile
import esprima
import math
from collections import Counter
from pathlib import Path
import sys
sys.setrecursionlimit(1500)

node_types = [
    'ArrayExpression', 'ArrowFunctionExpression', 'AssignmentExpression',
    'AwaitExpression', 'BinaryExpression', 'BlockStatement', 'CallExpression',
    'ConditionalExpression', 'ExpressionStatement', 'Identifier', 'IfStatement',
    'Literal', 'LogicalExpression', 'MemberExpression', 'NewExpression',
    'ObjectExpression', 'ObjectPattern', 'Program', 'Property', 'ReturnStatement',
    'TemplateElement', 'TemplateLiteral', 'UnaryExpression', 'Unknown',
    'VariableDeclaration', 'VariableDeclarator'
]

api_list = ['subprocess.send', 'zlib.deflate', 'fork', 'Certificate.exportChallenge', 'vm.runInNewContext', 'http2stream.sendTrailers', 'fs.fchmodSync', 'require.resolve', 'dns.setServers', 'http2stream.priority', 'fs.watch', 'socket.bind', 'console.table', 'cipher.setAutoPadding', 'path.relative', 'fs.openSync', 'fsPromises.stat', 'Agent', 'http2stream.respondWithFD', 'subprocess.ref', 'module.require', 'emitter.addListener', 'setTimeout', 'asyncHook.disable', 'tlsSocket.getEphemeralKeyInfo', 'agent.destroy', 'util.types.isDate', 'rl.question', 'urlSearchParams.forEach', 'fs.open', 'util.inspect', 'fs.unlink', 'hmac.digest', 'util.types.isWebAssemblyCompiledModule', 'buf.writeInt8', 'vm.Script', 'process.hasUncaughtExceptionCaptureCallback', 'tls.getCiphers', 'mknod', 'path.isAbsolute', 'fs.chmod', 'util.debug',
            'fs.readlink', 'trace_events.getEnabledCategories', 'readline.emitKeypressEvents', 'path.basename', 'util.isString', 'socket.setMulticastInterface', 'deserializer.readHeader', 'buf.writeUInt8', 'child_process.execFile', 'http.get', 'child_process.spawnSync', 'buf.writeDoubleBE', 'ecdh.computeSecret', 'performanceObserver.observe', 'child_process.execSync', 'stream.Duplex', 'socket.ref', 'urlSearchParams.getAll', 'async_hooks.executionAsyncId', 'emitter.off', 'zlib.deflateSync', 'net.Socket', 'console.info', 'util.types.isFloat64Array', 'process.getegid', 'dnsPromises.resolveNaptr', 'socket.destroy', 'util.getSystemErrorName', 'ECDH.convertKey', 'util.isNullOrUndefined', 'vm.compileFunction', 'getgid', 'server.close', 'urlSearchParams.toString', 'buf.writeInt32LE', 'readline.createInterface', 'fs.fsyncSync',
            'request.end', 'dirent.isSocket', 'vm.runInThisContext', 'response.write', 'subprocess.unref', 'fsPromises.chmod', 'socket.write', 'Buffer.alloc', 'console.groupCollapsed', 'process.hrtime', 'crypto.createECDH', 'emitter.rawListeners', 'util.types.isWeakSet', 'Buffer.from', 'util.types.isDataView', 'deserializer.readDouble', 'util.puts', 'chown', 'fs.appendFile', 'immediate.ref', 'dnsPromises.lookupService', 'script.runInNewContext', 'process.getgroups', 'urlSearchParams.values', 'fs.mkdirSync', 'util.isError', 'util.isFunction', 'socket.close', 'request.removeHeader', 'tracing.enable', 'fs.symlinkSync', 'readable.isPaused', 'dlopen', 'getegid', 'cluster.fork', 'console.timelineEnd', 'fs.fdatasync', 'urlSearchParams.delete', 'urlSearchParams.entries', 'replServer.parseREPLKeyword', 'fsPromises.writeFile',
              'rl.resume', 'http2.getDefaultSettings', 'http2session.setTimeout', 'fs.lchownSync', 'util.types.isAsyncFunction', 'getuid', 'ecdh.getPrivateKey', 'subprocess.disconnect', 'util.isUndefined', 'v8.getHeapSpaceStatistics', 'process.cpuUsage', 'path.normalize', 'setImmediate', 'buf.writeFloatBE', 'child_process.spawn', 'buf.readUIntBE', 'stringDecoder.end', 'os.uptime', 'message.setTimeout', 'dns.resolveTxt', 'server.addContext', 'buf.toJSON', 'PerformanceObserver', 'socket', 'crypto.scrypt', 'socket.address', 'os.getPriority', 'response.writeHead', 'crypto.createCipheriv', 'path.format', 'crypto.setFips', 'net.isIP', 'socket.getRecvBufferSize', 'os.platform', 'http2.getUnpackedSettings', 'http2session.unref', 'fs.readFileSync', 'socket.setSendBufferSize', 'readable.wrap', 'fs.existsSync', 'stream.finished',
                'zlib.deflateRaw', 'readable.setEncoding', 'fsPromises.open', 'transform._transform', 'filehandle.truncate', 'serializer._setTreatArrayBufferViewsAsHostObjects', 'util.isBuffer', 'fs.chown', 'fsPromises.readlink', 'http2session.ping', 'fs.ftruncateSync', 'console.markTimeline', 'socket.setEncoding', 'http.createServer', 'os.arch', 'buf.readDoubleLE', 'lchown', 'environ', 'buf.readUInt32BE', 'waitpid', 'socket.setMulticastTTL', 'util.types.isArrayBuffer', 'script.runInContext', 'request.getHeader', 'diffieHellman.getPrime', 'lstat', 'server.getTicketKeys', 'emitter.eventNames', 'certificate.verifySpkac', 'util.isArray', 'rename', 'performanceObserverEntryList.getEntriesByName', 'fs.unlinkSync', 'filehandle.readFile', 'buf.lastIndexOf', 'fs.futimesSync', 'stats.isSymbolicLink', 'fs.chownSync', 'net.isIPv6',
                  'decipher.final', 'crypto.createCipher', 'os.release', 'emitter.prependListener', 'server.address', 'EventEmitter.listenerCount', 'console.log', 'dns.resolve', 'util.types.isBigInt64Array', 'fs.chmodSync', 'dns.resolve4', 'crypto.createDecipher', 'cipher.final', 'tty.isatty', 'net.createConnection', 'console.count', 'process.emitWarning', 'console.error', 'os.setPriority', 'stream.Transform', 'utimes', 'buf.toString', 'seteuid', 'emitter.getMaxListeners', 'process.geteuid', 'serializer.writeDouble', 'assert.ifError', 'deserializer.readUint64', 'socket.setKeepAlive', 'util.types.isUint8ClampedArray', 'filehandle.read', 'writable.end', 'util.formatWithOptions', 'performance.now', 'process.initgroups', 'buf.copy', 'dirent.isDirectory', 'decipher.update', 'response.hasHeader', 'port.postMessage', 'buf.readIntLE',
                  'buf.writeUIntLE', 'util.isSymbol', 'crypto.privateDecrypt', 'filehandle.stat', 'querystring.unescape', 'util.types.isNumberObject', 'http2session.destroy', 'dirent.isFile', 'fs.readdirSync', 'performance.mark', 'crypto.scryptSync', 'tlsSocket.setMaxSendFragment', 'assert.strictEqual', 'process.setuid', 'util.types.isExternal', 'setuid', 'zlib.inflate', 'fs.renameSync', 'os.endianness', 'zlib.gunzip', 'http2stream.respond', 'worker.unref', 'console.countReset', 'util.types.isTypedArray', 'os.tmpdir', 'buf.readUInt8', 'fchown', 'transform.destroy', 'fs.lchmodSync', 'stream.Readable', 'stats.isFile', 'process.kill', 'process.setUncaughtExceptionCaptureCallback', 'fs.fstatSync', 'fs.fsync', 'readStream.setRawMode', 'stats.isDirectory', 'filehandle.datasync', 'assert.notDeepEqual', 'buf.readUInt32LE', 'response.getHeaders',
                  'fs.fchmod', 'Buffer.byteLength', 'buf.write', 'replServer.displayPrompt', 'worker.kill', 'timeout.ref', 'dnsPromises.resolveMx', 'Error', 'Buffer.isEncoding', 'buf.writeUInt32BE', 'session.disconnect', 'zlib.inflateSync', 'fs.statSync', 'crypto.createCredentials', 'replServer.clearBufferedCommand', 'socket.unref', 'performanceObserverEntryList.getEntries', 'diffieHellman.setPublicKey', 'buf.readInt8', 'buf.readFloatLE', 'vm.runInContext', 'buf.values', 'vm.createContext', 'net.connect', 'console.timeEnd', 'fs.appendFileSync', 'verify.update', 'crypto.createVerify', 'close', 'subprocess.kill', 'stats.isCharacterDevice', 'server.setTicketKeys', 'assert.notDeepStrictEqual', 'socket.setMulticastLoopback', 'tls.createServer', 'util.isDeepStrictEqual', 'zlib.createGunzip', 'path.parse', 'response.createPushResponse', 'buf.swap32',
                  'zlib.gzip', 'request.abort', 'eval', 'fs.writeFileSync', 'process.setgroups', 'url.format', 'fs.fchownSync', 'filehandle.sync', 'crypto.createSign', 'deserializer.readValue', 'dns.resolveMx', 'filehandle.utimes', 'dnsPromises.resolvePtr', 'console.profile', 'filehandle.close', 'util.types.isSetIterator', 'request.setHeader', 'fs.stat', 'socket.dropMembership', 'crypto.getDiffieHellman', 'performance.measure', 'process.disconnect', 'stats.isFIFO', 'zlib.createGzip', 'zlib.gzipSync', 'util.types.isWeakMap', 'readable.read', 'buf.writeDoubleLE', 'response.removeHeader', 'socket.getSendBufferSize', 'response.setHeader', 'util.error', 'buf.slice', 'port.ref', 'clearTimeout', 'crypto.privateEncrypt', 'fsPromises.mkdir', 'fs.createReadStream', 'fsPromises.truncate', 'emitter.emit', 'fs.readdir', 'zlib.createDeflateRaw', 'server.unref', 'response.end', 'process.setegid', 'zlib.createUnzip', 'buf.keys', 'crypto.createDecipheriv', 'zlib.gunzipSync', 'server.listen', 'readable.pause', 'buf.indexOf', 'fs.access', 'dnsPromises.resolveSoa', 'dnsPromises.resolveTxt', 'dns.resolve6', 'sign.sign', 'clearImmediate', 'buf.readInt16LE', 'fstat', 'dnsPromises.resolve6', 'util.log', 'module.instantiate', 'buf.readUInt16BE', 'console.timeline', 'assert', 'path.resolve', 'fsPromises.lstat', 'cipher.update', 'server.setTimeout', 'fs.readlinkSync', 'unlink', 'os.freemem', 'inspector.open', 'dns.resolveSrv', 'util.types.isProxy', 'stats.isBlockDevice', 'querystring.stringify', 'readable._destroy', 'os.loadavg', 'script.createCachedData', 'kqueue', 'buf.entries', 'os.userInfo', 'deserializer.readUint32', 'verify.verify', 'fsPromises.readdir', 'util.isNumber', 'fsPromises.symlink', 'fsPromises.lchmod', 'module.link', 'util.isNull', 'Certificate.verifySpkac', 'fsPromises.realpath', 'assert.rejects', 'dnsPromises.getServers', 'crypto.randomFill', 'dnsPromises.resolveSrv', 'dns.reverse', 'Buffer.allocUnsafeSlow', 'ecdh.setPrivateKey', 'fs.realpath.native', 'util.format', 'os.type', 'immediate.unref', 'url.parse', 'fsync', 'https.createServer', 'http2.connect', 'truncate', 'assert.fail', 'worker.isDead', 'fdatasync', 'crypto.publicEncrypt', 'writable.uncork', 'util.types.isRegExp', 'util.types.isSharedArrayBuffer', 'process.dlopen', 'crypto.createHash', 'util.print', 'dnsPromises.resolve', 'deserializer._readHostObject', 'urlSearchParams.sort', 'dnsPromises.resolveCname', 'process.seteuid', 'fs.rmdir', 'pwrite', 'console.timeLog', 'http2session.ref', 'socket.connect', 'v8.serialize', 'util.isDate', 'request.setSocketKeepAlive', 'hash.update', 'util.types.isGeneratorFunction', 'readable.unpipe', 'socket.setTTL', 'crypto.pbkdf2', 'fs.watchFile', 'util.promisify', 'dns.resolvePtr', 'console.trace', 'fs.lchmod', 'fsPromises.access', 'dns.resolveAny', 'buffer.transcode', 'util.isPrimitive', 'hmac.update',
                  'https.get', 'performance.timerify', 'path.toNamespacedPath', 'buf.writeInt16LE', 'urlSearchParams.append', 'buf.writeUInt32LE', 'fsPromises.link', 'writable.cork', 'readline.clearScreenDown', 'os.totalmem', 'crypto.createDiffieHellman', 'setsid', 'request.setNoDelay', 'util.types.isArgumentsObject', 'serializer._getSharedArrayBufferId', 'readable.resume', 'response.writeContinue', 'util.types.isSet', 'zlib.flush', 'serializer.writeValue', 'serializer._getDataCloneError', 'assert.doesNotReject', 'util.types.isSymbolObject', 'dirent.isCharacterDevice', 'performanceObserver.disconnect', 'certificate.exportPublicKey', 'fs.fdatasyncSync', 'console.dir', 'inspector.url', 'fs.exists', 'fs.link', 'setegid', 'os.homedir', 'response.writeProcessing', 'emitter.setMaxListeners', 'buf.readIntBE', 'fs.closeSync', 'tracing.disable', 'dirent.isSymbolicLink', 'writable._destroy', 'fsPromises.unlink', 'writable.write', 'worker.postMessage', 'response.setTimeout', 'fsPromises.lchown', 'util._extend', 'fs.utimesSync', 'util.types.isInt8Array', 'dns.lookup', 'http2stream.setTimeout', 'process.exit', 'emitter.listenerCount', 'fprintf', 'process.getgid', 'serializer.writeUint64', 'inotify', 'console.assert', 'http2stream.pushStream', 'dns.getServers', 'crypto.setEngine', 'crypto.Certificate', 'nsswitch.conf', 'os.networkInterfaces', 'resolv.conf', 'readline.clearLine', 'net.Server', 'v8.deserialize', 'zlib.createDeflate', 'querystring.parse', 'cluster.disconnect', 'setInterval', 'agent.getName', 'url.domainToASCII', 'stream.pipeline', 'net.isIPv4', 'buf.writeIntLE', 'fs.accessSync', 'ecdh.generateKeys', 'v8.setFlagsFromString', 'util.types.isInt32Array', 'path.extname', 'buf.readFloatBE', 'cipher.getAuthTag', 'console.groupEnd', 'Buffer.compare', 'message.destroy', 'crypto.timingSafeEqual', 'emitter.once', 'stat', 'AtExit', 'realpath', 'process.umask', 'fs.write', 'util.types.isMap', 'tlsSocket.getCipher', 'crypto.getCiphers', 'hash.digest', 'WebAssembly.instantiateStreaming', 'assert.notStrictEqual', 'async_hooks.createHook', 'asyncHook.enable', 'v8.cachedDataVersionTag', 'socket.setNoDelay', 'writable.destroy', 'performanceObserverEntryList.getEntriesByType', 'net.createServer', 'fsPromises.appendFile', 'script.runInThisContext', 'port.close', 'clearInterval', 'urlSearchParams.keys', 'serializer.writeUint32', 'fsPromises.readFile', 'server.getConnections', 'fs.truncateSync', 'buf.readUInt16LE', 'filehandle.appendFile', 'assert.deepStrictEqual', 'clienthttp2session.request', 'link', 'fsPromises.chown', 'tlsSocket.getTLSTicket', 'dnsPromises.resolve4', 'dnsPromises.resolveAny', 'dirent.isFIFO', 'serializer.releaseBuffer', 'rl.write', 'readlink', 'inspector.close', 'fs.mkdtemp', 'buf.writeInt16BE', 'agent.reuseSocket', 'geteuid', 'urlSearchParams.get', 'emitter.removeListener', 'emitter.prependOnceListener',
                  'buf.compare', 'fs.readFile', 'getaddrinfo', 'deserializer.transferArrayBuffer', 'process.chdir', 'dns.resolveCname', 'filehandle.chmod', 'fs.lchown', 'tlsSocket.address', 'buf.includes', 'trace_events.createTracing', 'session.connect', 'console.debug', 'deserializer.readRawBytes', 'fs.rename', 'writable._writev', 'socket.send', 'assert.doesNotThrow', 'rl.setPrompt', 'require.resolve.paths', 'worker.terminate', 'rmdir', 'tlsSocket.disableRenegotiation', 'fs.copyFileSync', 'response.addTrailers', 'fs.symlink', 'worker.send', 'console.dirxml', 'console.group', 'vm.isContext', 'writable._write', 'readline.moveCursor', 'agent.keepSocketAlive', 'textEncoder.encode', 'dns.resolveNs', 'cipher.setAAD', 'response.getHeaderNames', 'ecdh.setPublicKey', 'crypto.randomFillSync', 'util.types.isBigUint64Array', 'fs.linkSync', 'lchmod', 'console.clear', 'tlsSocket.getPeerCertificate', 'rl.close', 'emitter.listeners', 'url.resolve', 'util.types.isUint32Array', 'process.abort', 'fchmod', 'buf.readDoubleBE', 'replServer.defineCommand', 'fs.readSync', 'v8.getHeapStatistics', 'repl.start', 'process.getuid', 'serializer.writeRawBytes', 'assert.deepEqual', 'crypto.randomBytes', 'rl.prompt', 'tlsSocket.getFinished', 'util.inherits', 'worker.isConnected', 'util.types.isFloat32Array', 'decipher.setAuthTag', 'dnsPromises.resolveNs', 'fs.utimes', 'performance.clearMarks', 'assert.throws', 'Buffer.isBuffer', 'fs.rmdirSync', 'socket.pause', 'dnsPromises.setServers', 'fsPromises.mkdtemp', 'chmod', 'os.cpus', 'util.isRegExp', 'http2session.goaway', 'writable._final', 'crypto.getCurves', 'diffieHellman.getPublicKey', 'socket.setBroadcast', 'querystring.escape', 'async_hooks.triggerAsyncId', 'assert.notEqual', 'dnsPromises.lookup', 'process.hrtime.bigint', 'process.memoryUsage', 'fs.mkdir', 'crypto.createHmac', 'response.getHeader', 'util.types.isGeneratorObject', 'certificate.exportChallenge', 'path.join', 'Buffer.allocUnsafe', 'child_process.exec', 'fsPromises.rmdir', 'console.timeStamp', 'util.types.isInt16Array', 'buf.writeUInt16LE', 'http2stream.close', 'http2.getPackedSettings', 'crypto.publicDecrypt', 'tls.connect', 'console.warn', 'kill', 'buf.readUIntLE', 'util.types.isAnyArrayBuffer', 'port.unref', 'fs.truncate', 'request.flushHeaders', 'util.types.isUint16Array', 'readline.cursorTo', 'dns.resolveSoa', 'buf.readInt16BE', 'tlsSocket.getPeerFinished', 'require', 'path.dirname', 'util.deprecate', 'WebAssembly.compileStreaming', 'fs.lstatSync', 'transform._flush', 'fsPromises.utimes', 'zlib.createInflate', 'util.types.isMapIterator', 'exec', 'http2session.close', 'timeout.refresh', 'util.callbackify', 'serializer._writeHostObject', 'symlink', 'https.request', 'diffieHellman.getPrivateKey', 'filehandle.writeFile', 'fs.copyFile', 'crypto.getHashes', 'Worker', 'timeout.unref', 'tlsSocket.renegotiate', 'util.isBoolean',
                  'decipher.setAutoPadding', 'WebAssembly.compile', 'readable.pipe', 'tlsSocket.getSession', 'console.profileEnd', 'sign.update', 'zlib.inflateRawSync', 'util.debuglog', 'request.write', 'signal', 'curl', 'WebAssembly.instantiate', 'socket.setTimeout', 'http2.createSecureServer', 'fs.realpathSync.native', 'zlib.unzipSync', 'fs.ftruncate', 'fs.mkdtempSync', 'Certificate.exportPublicKey', 'zlib.params', 'readdir', 'deserializer.getWireFormatVersion', 'process.send', 'setgid', 'port.start', 'module.evaluate', 'os.hostname', 'url.domainToUnicode', 'fs.writeFile', 'filehandle.chown', 'crypto.pbkdf2Sync', 'readable.push', 'zlib.close', 'crypto.getFips', 'emitter.on', 'popen', 'diffieHellman.generateKeys', 'http.request', 'fs.createWriteStream', 'fs.realpathSync', 'fsPromises.rename', 'fs.fchown', 'agent.createConnection', 'stats.isSocket', 'console.time', 'rl.pause', 'util.types.isStringObject', 'process.cwd', 'tls.checkServerIdentity', 'fs.close', 'emitter.removeAllListeners', 'request.destroy', 'util.isObject', 'diffieHellman.setPrivateKey', 'process.nextTick', 'serializer.transferArrayBuffer', 'open', 'tls.createSecureContext', 'stringDecoder.write', 'readable.destroy', 'tlsSocket.getProtocol', 'socket.setRecvBufferSize', 'fs.fstat', 'urlSearchParams.has', 'util.types.isPromise', 'buf.fill', 'writeStream.getColorDepth', 'dns.lookupService', 'fs.lstat', 'http2session.settings', 'socket.end', 'dirent.isBlockDevice', 'zlib.inflateRaw', 'buf.writeFloatLE', 'buf.equals', 'buf.readInt32LE', 'child_process.fork', 'serverhttp2session.altsvc', 'urlSearchParams.set', 'fs.writeSync', 'util.types.isNativeError', 'buf.writeUIntBE', 'process.setgid', 'writable.setDefaultEncoding', 'util.types.isModuleNamespaceObject', 'http2.createServer', 'http2stream.respondWithFile', 'diffieHellman.getGenerator', 'server.ref', 'mkdir', 'session.post', 'fs.realpath', 'assert.ok', 'serializer.writeHeader', 'buf.swap64', 'Error.captureStackTrace', 'child_process.execFileSync', 'request.setTimeout', 'assert.equal', 'uname', 'process.uptime', 'url.toString', 'fs.futimes', 'diffieHellman.computeSecret', 'zlib.createInflateRaw', 'worker.ref', 'http2stream.additionalHeaders', 'ecdh.getPublicKey', 'buf.swap16', 'dgram.createSocket', 'readable.unshift', 'buf.readInt32BE', 'util.types.isUint8Array', 'read', 'buf.writeInt32BE', 'buf.writeUInt16BE', 'readable._read', 'socket.resume', 'fsPromises.copyFile', 'zlib.deflateRawSync', 'resolver.cancel', 'fs.read', 'textDecoder.decode', 'zlib.unzip', 'dns.resolveNaptr', 'util.types.isBooleanObject', 'worker.disconnect', 'cluster.setupMaster', 'Buffer.concat', 'dnsPromises.reverse', 'url.toJSON', 'buf.writeIntBE', 'fs.unwatchFile', 'socket.addMembership', 'decipher.setAAD', 'filehandle.write', 'Discord.Client','client.billing.fetchPaymentSources','phin','stream.pipe','stream.on','document.addEventListener','fetch']

def calculate_normalized_entropy(text):
    character_freq = {}
    total_characters = len(text)
    for char in text:
        character_freq[char] = character_freq.get(char, 0) + 1

    entropy = 0
    for freq in character_freq.values():
        probability = freq / total_characters
        entropy += -probability * math.log(probability, 2)

    if entropy == 0:
        return 0
    normalized_entropy = entropy / math.log(len(character_freq), 2)
    return normalized_entropy

def check_api_usage(node, api_usage, visited_nodes):
    if isinstance(node, dict):
        node_id = id(node)
        if node_id in visited_nodes:
            return
        visited_nodes.add(node_id)

        node_type = node.get('type')
        if node_type == 'CallExpression':
            callee = node.get('callee')
            process_callee(callee, api_usage)

        for value in node.values():
            if isinstance(value, dict):
                check_api_usage(value, api_usage, visited_nodes)
            elif isinstance(value, list):
                for item in value:
                    check_api_usage(item, api_usage, visited_nodes)

def process_callee(callee, api_usage):
    if isinstance(callee, dict):
        if callee.get('type') == 'MemberExpression':
            process_member_expression(callee, api_usage)
        elif callee.get('type') == 'Identifier' and callee.get('name') in api_list:
            api_usage[callee.get('name')] += 1

def process_member_expression(member_expr, api_usage):
    object_part = member_expr.get('object')
    property_part = member_expr.get('property')
    if isinstance(object_part, dict) and isinstance(property_part, dict):
        object_name = object_part.get('name')
        property_name = property_part.get('name')
        full_name = f"{object_name}.{property_name}"
        if full_name in api_list:
            api_usage[full_name] += 1

def extract_ast_from_js_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(file_path)
            ast = esprima.parseScript(content, {'tolerant': True, 'ecmaVersion': 2020})

            return ast, content
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None, None

def traverse_node(node, node_types, api_usage, visited_nodes):
    nodes = []
    max_depth = 0
    stack = [(node, 0)]

    while stack:
        current_node, depth = stack.pop()
        max_depth = max(max_depth, depth)

        node_dict = current_node.toDict() if hasattr(current_node, 'toDict') else current_node

        check_api_usage(node_dict, api_usage, visited_nodes)
        node_type = node_dict.get('type', 'Unknown')
        if node_type in node_types:
            nodes.append(node_type)

        for value in node_dict.values():
            if isinstance(value, (dict, esprima.nodes.Node)):
                stack.append((value, depth + 1))
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, (dict, esprima.nodes.Node)):
                        stack.append((item, depth + 1))

    return nodes, max_depth

def process_js_file(file_path, node_types, api_list):
    ast, content = extract_ast_from_js_file(file_path)
    if ast is not None and content is not None:
        api_usage = {api: 0 for api in api_list}
        visited_nodes = set()
        node_types_found, max_depth = traverse_node(ast, node_types, api_usage, visited_nodes)
        entropy = calculate_normalized_entropy(content)
        #label = get_label_from_folder_path(file_path)
        return Counter(node_types_found), api_usage, entropy, max_depth
    else:
        return None

def write_to_csv(data, headers, csv_file):
    mode = 'a' if os.path.exists(csv_file) else 'w'
    with open(csv_file, mode, newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if mode == 'w':
            writer.writerow(headers)
        writer.writerows(data)

        
# GitHub에서 npm 패키지 목록을 가져오는 함수
def fetch_package_list():
    url = "https://api.github.com/search/repositories?q=topic:npm&per_page=100"
    response = requests.get(url)
    response.raise_for_status()
    repositories = response.json()["items"]
    package_list = [repo["full_name"] for repo in repositories]
    return package_list

# 저장소의 기본 브랜치를 가져오는 함수
def get_default_branch(repo_full_name):
    url = f"https://api.github.com/repos/{repo_full_name}"
    response = requests.get(url)
    if response.status_code == 200:
        repo_info = response.json()
        return repo_info.get("default_branch", "main")
    return "main"

# 실제 npm 패키지 이름을 가져오는 함수
def get_npm_package_name(repo_full_name):
    branches = ['main', 'master']
    paths = ['', 'src/', 'lib/', 'dist/']
    for branch in branches:
        for path in paths:
            url = f"https://raw.githubusercontent.com/{repo_full_name}/{branch}/{path}package.json"
            response = requests.get(url)
            if response.status_code == 200:
                package_info = response.json()
                return package_info.get("name")
    return None

# npm 레지스트리에서 패키지 존재 여부를 확인하는 함수
def is_package_in_npm_registry(package_name):
    url = f"https://registry.npmjs.org/{package_name}"
    response = requests.get(url)
    return response.status_code == 200

# 패키지를 임시 폴더에 다운로드하는 함수
def download_package_in_temp(package_name):
    temp_dir = tempfile.mkdtemp()
    try:
        subprocess.run(["npm", "pack", package_name], cwd=temp_dir, check=True)
        # 다운로드한 파일 찾기
        package_files = [f for f in os.listdir(temp_dir) if f.endswith(".tgz") or f.endswith(".tar.gz") or f.endswith(".zip")]
        if not package_files:
            raise FileNotFoundError(f"No package file found for {package_name}")
        
        package_file = os.path.join(temp_dir, package_files[0])
        extracted_path = tempfile.mkdtemp()

        # 압축 해제
        if package_file.endswith(".tgz") or package_file.endswith(".tar.gz"):
            with tarfile.open(package_file, "r:gz") as tar:
                tar.extractall(path=extracted_path)
        elif package_file.endswith(".zip"):
            with zipfile.ZipFile(package_file, "r") as zip_ref:
                zip_ref.extractall(extracted_path)
        else:
            raise ValueError(f"Unknown package format: {package_file}")

        # .js 파일이 있는 디렉토리 찾기
        js_files = []
        for root, _, files in os.walk(extracted_path):
            for file in files:
                if file.endswith(".js"):
                    js_files.append(os.path.join(root, file))
        
        if not js_files:
            raise FileNotFoundError(f"No .js files found in package {package_name}")

        return extracted_path, js_files
    except Exception as e:
        shutil.rmtree(temp_dir)
        raise e

# 임시 폴더를 삭제하는 함수
def delete_package_in_temp(package_path):
    shutil.rmtree(package_path)
    
filtered = ['./data/benign/npm/TypeScript/tests/baselines/reference/binderBinaryExpressionStress.js']


# 패키지를 분석하는 함수 (사용자 정의 분석 모델 사용)
def analyze_package_in_temp(tmp_path, filtered, node_types, api_list, url, package_name):
    ast_data = []
    
    for root, dirs, files in os.walk(tmp_path):
        for file in files:
            if file.endswith(".js"):
                file_path = os.path.join(root, file)
                if file_path in filtered:
                    continue
                result = process_js_file(file_path, node_types, api_list)
                if result:
                    node_counts, api_usage, entropy, max_depth = result
                    row = [None, url, package_name, file, entropy, max_depth] + [node_counts[node_type] for node_type in node_types] + [api_usage[api] for api in api_list]
                    ast_data.append(row)

    csv_file = "analyzed_packages3.csv"
    headers = ['Label','URL', 'package', 'Filename', 'Entropy', 'MaxDepth'] + node_types + api_list
    write_to_csv(ast_data, headers, csv_file)


# 메인 함수
def main():
    package_list = fetch_package_list()
    while package_list:
        repo_full_name = random.choice(package_list)
        package_name = get_npm_package_name(repo_full_name)
        if not package_name:
            print(f"Could not determine package name for {repo_full_name}")
            package_list.remove(repo_full_name)
            continue
        
        if not is_package_in_npm_registry(package_name):
            print(f"Package {package_name} not found in npm registry")
            package_list.remove(repo_full_name)
            continue

        try:
            temp_path, js_files = download_package_in_temp(package_name)
            if not js_files:
                print(f"Failed to process {package_name}: No .js files found in package {package_name}")
                delete_package_in_temp(temp_path)
                package_list.remove(repo_full_name)
                continue
            
            url = f"https://github.com/{repo_full_name}"
            analyze_package_in_temp(temp_path, filtered, node_types, api_list, url, package_name)
            delete_package_in_temp(temp_path)
            print(f"Successfully processed {package_name}")
        except FileNotFoundError as e:
            print(f"Failed to process {package_name}: {e}")
        except Exception as e:
            print(f"An error occurred while processing {package_name}: {e}")
        package_list.remove(repo_full_name)


# 스크립트 실행
if __name__ == "__main__":
    main()

