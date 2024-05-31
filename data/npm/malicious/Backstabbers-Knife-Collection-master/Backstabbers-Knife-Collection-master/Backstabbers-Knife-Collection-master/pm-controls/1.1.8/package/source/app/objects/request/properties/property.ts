import { 
    ComponentFactory,
    Input
} from '@angular/core';
import { PropertyLabel } from '../../../objects/request/property-label';
import { Orientation } from '../../../objects/enums/orientation';
import { Validation } from '../../../objects/validation/validation';

export class Property {
    constructor(
        public Label: PropertyLabel,
        orientation?: Orientation,
        public IsHidden?: boolean,
        public IsDisabled?: boolean) {
            
        this.Validation = new Validation();
        if (orientation)
            this.Orientation = orientation;
        else
            this.Orientation = Orientation.Vertical;
    }

    Validation: Validation;
    Orientation: Orientation;
    
    get Type(): string {
        if (this.IsCheckBox)
            return "CheckBox";
        if (this.IsComboBox)
            return "ComboBox";
        if (this.IsCheckBoxComboBox)
            return "CheckBoxComboBox";              
        if (this.IsDatePicker)
            return "DatePicker";
        if (this.IsDateRangePicker)
            return "DateRangePicker";
        if (this.IsMultiSelectTextBox)
            return "MultiSelectTextBox";                
        if (this.IsNumericBox)
            return "NumericBox";
        if (this.IsTextarea)
            return "TextArea";
        if (this.IsTextBox)
            return "TextBox";
        if (this.IsRadioGroup)
            return "RadioButton";
        if (this.IsTemplate)
            return "Template";

        return "";
    }

    IsCheckBox: boolean;
    IsComboBox: boolean;
    IsCheckBoxComboBox: boolean;
    IsDatePicker: boolean;
    IsDateRangePicker: boolean;
    IsDateTimePicker: boolean;
    IsNumericBox: boolean;
    IsMultiSelectTextBox: boolean;
    IsTextarea: boolean;
    IsTextBox: boolean;
    IsRadioGroup: boolean;
    IsTemplate: boolean;

    Clear() { }
    DefaultValidation() { }
}