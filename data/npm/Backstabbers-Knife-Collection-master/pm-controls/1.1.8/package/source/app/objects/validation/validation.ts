export class Validation {

    HasValidation: boolean;
    Error: string;

    public Set(message: string)
    {
        this.Error = message;
        this.HasValidation = true;
    }

    public Clear()
    {
        this.Error = "";
        this.HasValidation = false;
    }
 }