'use strict';

(function ($) {
    $.fn.uploaderGallery = function(options) {

        var $that       = this;
        var defaults    = {
            // These are the defaults.
            title: 'Drop Here',
            classes: "",

            showbtn: false,
            btnClasses: "",
            btnTitle: 'Add Files',

            thumbClasses: "",
            thumbDeleteIcon: "fa fa-times",
            thumbDeleteBtnClass: "",
            thumbImgClasses: "",
            thumbPrevHtml: "",
            thumbNextHtml: "",

            mimetypes: "", // Separate types by pip |

            submitFormTrigger: false,
            ajaxSubmit: function() {}
        };

        // This is the easiest way to have default options.
        var settings = $.extend({}, defaults, options);

        // First check if File is avaiable in browser
        function checkFileAvaiable() {
            return (w.File && w.FileList && w.FileReader);
        }

        if (!checkFileAvaiable) {
            console.log('File not avaibale')
            return false;
        }

        // check if uploader container not exist prepend one
        function uploaderContainer() {
            if ($that.parent().find('#uploader-gallery').length == 0) {
                $that.parent().prepend('<div id="uploader-gallery" class="uploader-gallery"></div>');
            }

            var classes = prepareClasses(settings.classes);
            $that.attr('name', 'images'); // change name for fixing push image to input file problem 
            return $that.hide().parent().find('#uploader-gallery').addClass(classes).attr('data-title', settings.title);
        }

        // initialization 
        function init() {
            prepare();
            actions();

            if (settings.showbtn)
                addBtn()

            checkThumbHideBtn();
        }

        // prepare classes 
        function prepareClasses(classes) {
            return (Array.isArray(classes)) ? classes.join(' ') : classes
        }

        // add btn 
        function addBtn() {
            var classes = prepareClasses(settings.btnClasses);

            $that.uploaderContainer.append('<a class="btn btn-success ' + classes + ' uploader-btn">' + settings.btnTitle + '</a>');
        }

        // prepare values
        function prepare() {
            $that.uploaderContainer = uploaderContainer(),
                $that.deleteBtn = $that.uploaderContainer.find('.delete-img'),
                $that.form = $that.closest('form'),
                $that.uploadBtn = $that.uploaderContainer.find('uploader-btn'),
                $that.files = [];
        }

        // actions
        function actions() {
            $that.uploaderContainer.on('click', function() {
                $that.trigger('click');
            });

            $that.uploadBtn.on('click', function() {
                $that.trigger('click');
            })

            // handle drag event
            $that.uploaderContainer.on('dragover', handleDragOver)
            $that.uploaderContainer.on('drop', handleDropFiles)
            // handle file select by input
            $that.on('change', handleFileSelect);

            // check if submit form trigger is on of not
            if( settings.submitFormTrigger )
                $that.form.on('submit', { files: $that.files }, settings.ajaxSubmit);
        }

        function handleDragOver(e) {
            e.preventDefault();
            e.stopPropagation();
            e.originalEvent.dataTransfer.dropEffect = 'copy';
        }

        // check to hide add btn
        function checkThumbHideBtn() {
            if ($('.thumb-container').length > 0) {
                $that.uploaderContainer.attr('data-title', '');
                $('a.uploader-btn').hide();
            } else {
                $that.uploaderContainer.attr('data-title', settings.title);
                $('a.uploader-btn').show();
            }
        }

        /**
         * Handle the draging and droping of files
         * Check extension then drawing them 
         */
        function handleDropFiles(e) {
            e.stopPropagation();
            e.preventDefault();

            var files = e.originalEvent.dataTransfer.files;
            
            if( checkFileExtenstion(files) == false )
                alert('Extenstions allowed: ' + settings.mimetypes );
            else 
                _draw.init(files);
        }


        /**
         * Check file extenstion 
         * Based on mimeTypes
         */
        function checkFileExtenstion(files) {
            var types = settings.mimetypes.split('|'),
                valid = true;

            jQuery.each(files, function (index, file) {
                if( types.indexOf(file.type) === -1 )
                    valid = false;
            })

            return valid;
        }
        
        /**
         * Handle file select of input file
         * check if files are allowed
         */
        function handleFileSelect(e) {
            var files = e.target.files;

            if( checkFileExtenstion(files) == false )
                alert('Extenstions allowed: ' + settings.mimetypes );
            else 
                _draw.init(files);
        }

        /**
         * Remove thumbs
         *
         */
        function removeThumb(e) {
            e.stopPropagation();

            $that.files.splice($(this).data('index'), 1);
            $(this).parent().fadeOut(300, function() {
                $(this).remove();

                checkThumbHideBtn();
            });
        }

        var _draw = {

            // handle drawing of items
            init: function (files) {
                var that = this;
                for (var i = 0, f; f = files[i]; i++) {

                    var index   = that.push(f),
                        reader  = new FileReader(),
                        $html   = '';

                    reader.onload = (function(theFile) {
                        return function(e) {
                            var imgClasses  = prepareClasses(settings.thumbImgClasses);

                            $html = that.drawBefore($html);
                            $html = that.drawDelBtn($html, index);
                            $html += '<img src="' + e.target.result + '" width="100" height="150" class="' + imgClasses + '">';
                            $html = that.drawAfter($html)

                            $('#uploader-gallery').append($html);
                            $('.delete-img-new').on('click', removeThumb);
                        };
                    })(f);

                    reader.readAsDataURL(f);

                    checkThumbHideBtn();
                }
            },
            // push file to files array 
            push: function (file) {
                return $that.files.push(file);
            },
            // draw before image html
            drawBefore: function (html) {
                var mainClasses = prepareClasses(settings.thumbClasses);
                    
                html += '<div class="thumb-container ' + mainClasses + '">';

                html += settings.thumbPrevHtml;

                return html;
            },
            // draw after image html
            drawAfter: function (html) {
                // custom html
                html += settings.thumbNextHtml;
                // End custom html

                html += '</div>';

                return html;
            },
            // draw delete button
            drawDelBtn: function(html, index) {
                var delClasses  = prepareClasses(settings.thumbDeleteBtnClass);

                // End Custom Html
                html += '<span class="delete-img-new ' + delClasses + '" data-index="' + --index + '"> <i class="' + settings.thumbDeleteIcon + '"> </i></span>';

                return html;
            }
        }

        init();

        return this;
    }
    
})(jQuery);
