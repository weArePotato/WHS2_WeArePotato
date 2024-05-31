import { TooltipComponent } from '../../components/tooltips/tooltip-component';
export declare class TooltipDirective {
    tooltip: TooltipComponent;
    stillHover: boolean;
    hoverKey: number;
    x: number;
    y: number;
    mouseMove(event: MouseEvent): void;
    onTooltip(event: MouseEvent): void;
    DurationTimer(localKey: number): void;
    offTooltip(event: MouseEvent): void;
    ngOnInit(): void;
}
