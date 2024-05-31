
import functionsIn = require('lodash/functionsIn')
interface ErrorConstructor {
    prepareStackTrace(error?:any, structuredStackTrace?:any):any[];
}
interface ErrorStack
{
    getTypeName(): string;
    getFunctionName(): string;
    getMethodName(): string;
    getFileName(): string;
    getTypeName(): string;
    getLineNumber(): number;
    getColumnNumber(): number;
    isNative(): boolean;
}
interface ErrorWithStack  {
    stack: ErrorStack;
    name: string;
    message: string;
}

declare function require();


declare var _:any;
