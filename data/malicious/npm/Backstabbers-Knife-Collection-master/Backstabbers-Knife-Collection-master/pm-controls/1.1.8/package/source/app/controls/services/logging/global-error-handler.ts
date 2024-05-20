import {
  ErrorHandler, 
  Injectable
} from '@angular/core';
import { ErrorToast } from '../../../controls/services/logging/error-toast';
import { ControlsModule } from '../../../controls/controls-module';

@Injectable()
export class GlobalErrorHandler extends ErrorHandler {

  handleError(error: any) {    
    var errorToast = <ErrorToast>ControlsModule.toast.Show(ErrorToast);
    
    if (!errorToast) {
      console.log(error);
      return;
    }

    var item = <Error>error;
    if (error instanceof Error) {
      errorToast.Name = item.name;
      errorToast.Message = item.message;
      errorToast.Stack = item.stack;
    } else {
      errorToast.Name = error;
    }
    errorToast.RaiseChange();
    super.handleError(error);  
  }
}