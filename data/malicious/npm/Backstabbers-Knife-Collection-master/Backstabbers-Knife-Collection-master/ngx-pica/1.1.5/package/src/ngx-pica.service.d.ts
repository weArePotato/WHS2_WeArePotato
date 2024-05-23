import { Observable } from 'rxjs/Observable';
import { NgxPicaResizeOptionsInterface } from './ngx-pica-resize-options.interface';
import { NgxPicaExifService } from './ngx-pica-exif.service';
export declare class NgxPicaService {
    private _ngxPicaExifService;
    private picaResizer;
    private MAX_STEPS;
    constructor(_ngxPicaExifService: NgxPicaExifService);
    /**
     * Resize images array
     * @param {File[]} files
     * @param {number} width
     * @param {number} height
     * @param {NgxPicaResizeOptionsInterface} options
     * @returns {Observable<File>}
     */
    resizeImages(files: File[], width: number, height: number, options?: NgxPicaResizeOptionsInterface): Observable<File>;
    /**
     * Resize image file
     *
     * @param {File} file
     * @param {number} width
     * @param {number} height
     * @param {NgxPicaResizeOptionsInterface} options
     * @returns {Observable<File>}
     */
    resizeImage(file: File, width: number, height: number, options?: NgxPicaResizeOptionsInterface): Observable<File>;
    /**
     * Compress images array
     *
     * @param {File[]} files
     * @param {number} sizeInMB
     * @returns {Observable<File>}
     */
    compressImages(files: File[], sizeInMB: number): Observable<File>;
    /**
     * Compress image file
     *
     * @param {File} file
     * @param {number} sizeInMB
     * @returns {Observable<File>}
     */
    compressImage(file: File, sizeInMB: number): Observable<File>;
    /**
     * Through Pica toBlob method, compress image file
     *
     * @param {HTMLCanvasElement} canvas
     * @param {string} type
     * @param {number} quality
     * @param {number} sizeInMB
     * @param {number} step
     * @returns {Promise<Blob>}
     */
    private getCompressedImage(canvas, type, quality, sizeInMB, step);
    /**
     * Check if image has been compressed enough
     *
     * @param {HTMLCanvasElement} canvas
     * @param {Blob} blob
     * @param {number} quality
     * @param {number} sizeInMB
     * @param {number} step
     * @returns {Promise<Blob>}
     */
    private checkCompressedImageSize(canvas, blob, quality, sizeInMB, step);
    /**
     * Through Pica resize method, resize image file
     *
     * @param {File} file
     * @param {HTMLCanvasElement} from
     * @param {HTMLCanvasElement} to
     * @param options
     * @returns {Promise<File>}
     */
    private picaResize(file, from, to, options);
    /**
     * Return new File from Blob
     *
     * @param {Blob} blob
     * @param {string} name
     * @param {string} type
     * @param {number} lastModified
     * @returns {File}
     */
    private blobToFile(blob, name, type, lastModified);
    /**
     * Convert bytes to MegaBytes
     *
     * @param {number} bytes
     * @returns {number}
     */
    private bytesToMB(bytes);
}
