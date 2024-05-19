export class ElementExtensions {
    static width(item: any): number {
        if (item) {
            if (item.nativeElement)            
                return item.nativeElement.offsetWidth;
            
            return item.offsetWidth;
        }
        return 0;
    }

    static height(item: any): number {
        if (item) {
            if (item.nativeElement)
            {
                if (item.nativeElement.clientHeight == 0)
                    return item.nativeElement.offsetHeight;
                return item.nativeElement.clientHeight;
            }
            
            if (item.clientHeight == 0)
                return item.offsetHeight;

            return item.clientHeight;
        }
        return 0;
    }

    static scrollWidth(item: any): number {
        if (item) {
            if (item.nativeElement)
                return item.nativeElement.scrollWidth;
            
            return item.scrollWidth;
        }
        return 0;
    }

    static scrollHeight(item: any): number {
        if (item) {
            if (item.nativeElement)
                return item.nativeElement.scrollHeight;
            
            return item.scrollHeight;
        }
        return 0;
    }

    static parsePx(item: any): number {
        return parseInt(item, 10);
    }

    static getParentScrollTop(item: any): number {

        if (item) {
            if (item.scrollTop > 0)
                return item.scrollTop;
            return ElementExtensions.getParentScrollTop(item.parentElement);
        }

        return 0;
    }
}