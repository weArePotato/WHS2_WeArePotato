import { Dictionary } from "../../objects/dictionary";
import { Property } from "../../objects/request/properties/property";
import { Column } from "../../objects/request/column";

export class BaseRequest {

    public Properties: Dictionary<Property> = new Dictionary<Property>();
    public Columns: Dictionary<Column> = new Dictionary<Column>();

    public Validate() {

        for (let property of this.Properties.Values) {
            property.Validation.Clear();
        }

        this.Validation();

        for (let property of this.Properties.Values) {
            property.DefaultValidation();
        }

        for (let property of this.Properties.Values) {
            if (property.Validation.HasValidation)
                return false;
        }

        return true;
    }

    protected Validation() { }

    public ClearProperties() {
        for (let property of this.Properties.Values) {
            property.Clear();
            property.Validation.Clear();
        }
    }

    public ClearValidation() {
        for (let property of this.Properties.Values) {
            property.Validation.Clear();
        }
    }
 }