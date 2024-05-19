import { RadioGroupItem } from "../../../objects/request/radio-group/radio-group-item";



export class RadioGroup {
    constructor() {

        this.Items = [
            new RadioGroupItem(false, "testing 1", false),
            new RadioGroupItem(true, "testing 2", false)
        ]
        //     var items = new Array<RadioGroupItem>();
        //     var item1 = new RadioGroupItem(false, "testing 1", false);
        //     var item2 = new RadioGroupItem(true, "testing 2", false);

        //     items.push(item1);
        //     items.push(item2);
        //     return items;
        // }
     }

    public Items;
}