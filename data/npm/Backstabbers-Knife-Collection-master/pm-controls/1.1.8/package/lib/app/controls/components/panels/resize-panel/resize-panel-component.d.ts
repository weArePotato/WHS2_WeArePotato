import { Orientation } from '../../../../objects/enums/orientation';
export declare class ResizePanelComponent {
    HeightPx: any;
    Orientation: Orientation;
    FirstElementFlexGrow: number;
    SecondElementFlexGrow: number;
    CustomThumbClass: string;
    readonly Height: string;
    flexDirection(): "row" | "column";
    isHorizontal(): boolean;
    logDragStart($event: any): void;
}
