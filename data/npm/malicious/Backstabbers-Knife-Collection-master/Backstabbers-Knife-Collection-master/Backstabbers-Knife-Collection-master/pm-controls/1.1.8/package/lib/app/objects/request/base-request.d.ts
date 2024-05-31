import { Dictionary } from "../../objects/dictionary";
import { Property } from "../../objects/request/properties/property";
import { Column } from "../../objects/request/column";
export declare class BaseRequest {
    Properties: Dictionary<Property>;
    Columns: Dictionary<Column>;
    Validate(): boolean;
    protected Validation(): void;
    ClearProperties(): void;
    ClearValidation(): void;
}
