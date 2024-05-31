import { PropertyLabel } from '../../../objects/request/property-label';
import { Orientation } from '../../../objects/enums/orientation';
import { Validation } from '../../../objects/validation/validation';
export declare class Property {
    Label: PropertyLabel;
    IsHidden: boolean;
    IsDisabled: boolean;
    constructor(Label: PropertyLabel, orientation?: Orientation, IsHidden?: boolean, IsDisabled?: boolean);
    Validation: Validation;
    Orientation: Orientation;
    readonly Type: string;
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
    Clear(): void;
    DefaultValidation(): void;
}
