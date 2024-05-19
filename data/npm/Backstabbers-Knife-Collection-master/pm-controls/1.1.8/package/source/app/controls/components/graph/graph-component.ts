import { Output, EventEmitter, Component, Input, Renderer, ElementRef,ViewChild, OnChanges, ChangeDetectionStrategy, SimpleChange } from '@angular/core';
import * as d3 from '../../../../bundles/d3-bundle';
import * as Immutable from 'immutable';
import * as _ from 'lodash';
import { TimeSeries, TimeSeriesItem } from '../../../objects/time-series/time-series';
import { Margin } from '../../../objects/margin';

@Component({
    selector: 'pm-graph',
    //templateUrl: './app/controls/components/graph/graph-component.html',
    templateUrl: './graph-component.html',
    styles: [`
  :host { 
    position: relative;
    display: block;
  }`],    
    changeDetection: ChangeDetectionStrategy.OnPush
})
export class GraphComponent implements OnChanges {

    @Input() lineData: Immutable.List<TimeSeries>;
    @Input() pointData: Immutable.List<TimeSeries>;
    @Input() height: number = 500;
    @Input() width: number = 960;
    @Input() includeLineDataPoints: boolean = true;
    @Input() includeHoverLine: boolean = true;
    @Input() hoverLineDisplay: (dataPoint: {
        "datePos": Date;
        "values": Immutable.Iterable<number, {
            "seriesName": string;
            "value": TimeSeriesItem;
        }>;
    }) => string;
    @Input() transitionDuration: number = 300; // in milliseconds
    @Input() hideBorder: boolean = false;
    @Input() yAxisTitle: string;
    @Input() ySecondAxisTitle: string;
    @Input() interpolationMethod: d3.CurveFactory = d3.curveLinear;
    @Input() margin: Margin = { top: 0, right: 70, bottom: 100, left: 70 };
    @Input() xAxisTextRotation: string = "-45";
    @Input() yAxisSecondAxisDataFilter: any; // method that returns true/false. True if data is for 2nd Y-axis;
    @Input() AllowZoomX: boolean = true;
    @Input() AllowZoomY : boolean= true;
    @Input() xExtent : [Date,Date];

    // includes an area that displays the difference between the first 2 TimeSeries in the linedData.
    @Input() IncludeDifference : boolean = false;

    @Input() disableWheelZoom: boolean = false;

    @Input() UseContinuousHoverLine: boolean = false;

    @Input() xDomain: [Date, Date] = null;
    @Input() yDomain: [number, number]= null;
    @Input() useTweenTransition: false;

    @Input() lineSizePx: string = "1px";
    @Input() pointSizeR: number = 3;

    @Input() userColors: string[];

    @Input() UniqueId: string = "0"; // unique ID to identify this graph. Necessary for the clip-path URL used for the differences.

    @Output() TooltipItemChange: EventEmitter<any> = new EventEmitter<any>();

    @ViewChild('tooltip') tooltipElementRef: ElementRef;

    private svg: any;
    private x: d3.ScaleTime<any, any>;
    private y: d3.ScaleLinear<number, number>;
    private y2: d3.ScaleLinear<number, number>;
    private zoomedX: d3.ScaleTime<any, any>;
    private zoomedY: d3.ScaleLinear<number, number>;
    private zoomedY2: d3.ScaleLinear<number, number>;
    private graphContainer: any;

    private color: d3.ScaleOrdinal<string, string>;

    private xAxis: d3.Axis<any>;
    private yAxis: d3.Axis<any>;
    private y2Axis: d3.Axis<any>;

    private line: d3.Line<TimeSeriesItem>;
    private area: d3.Area<TimeSeriesItem>;
    private differenceArea: d3.Area<any>;

    private tooltip: d3.Selection<any, any, any, any>;

    private hoverLine: d3.Selection<any, any, any, any>;

    private isZoomButtonUpdate: boolean = false;

    private zoom: d3.ZoomBehavior<any, any>;
    private flattenedItems: Array<[TimeSeriesItem, string]>;
    private flattenedPointItems: Array<[TimeSeriesItem, string]>; 
    private flattenedItemsAxis2: Array<[TimeSeriesItem, string]>;
    private mutableData: TimeSeries[];
    private mutableDataAxis1: TimeSeries[];
    private mutableDataAxis2: TimeSeries[];

    private differenceData : any;

    private mutablePointData: TimeSeries[];


    private zoomPane: any;

    constructor(private el: ElementRef) {
    }

    ngOnChanges(changeDetection: any) {
        if (changeDetection.lineData !== undefined || changeDetection.pointData !== undefined)
            this.handleDataChange(changeDetection.lineData, changeDetection.pointData);
    }

    handleDataChange(dataChange: SimpleChange, pointChange :SimpleChange) {
        if ((!dataChange || !dataChange.currentValue) && (!pointChange || !pointChange.currentValue)) return;

        if (!this.lineData)
            this.lineData = Immutable.List<TimeSeries>();

        this.mutableData = this.lineData.toArray();

        if(!this.pointData)
            this.pointData = Immutable.List<TimeSeries>();

        this.mutablePointData = this.pointData.toArray();

        this.mutableDataAxis1 = this.yAxisMutableData();
        this.mutableDataAxis2 = this.yAxis2MutableData();

        if(this.IncludeDifference && this.mutableData.length>1) {
            var index0 = 0;
            var index1 = 0;
            var list0Done = () => index0 == this.mutableData[0].Data.length;
            var list1Done = () => index1==this.mutableData[1].Data.length;
            this.differenceData = [];

            while (!list0Done() || !list1Done()) {                
                if (this.mutableData[0].Data[index0].Date.getTime() < this.mutableData[1].Data[index1].Date.getTime() || list1Done()) {
                    this.differenceData.push(
                        {
                            Date: this.mutableData[0].Data[index0].Date,
                            Value0: this.mutableData[0].Data[index0].Value,
                            Value1: index1 == 0 ? 0 : this.mutableData[1].Data[list1Done() ? this.mutableData[1].Data.length-1: index1-1].Value
                        });
                    index0++;
                }
                else if (this.mutableData[0].Data[index0].Date.getTime() > this.mutableData[1].Data[index1].Date.getTime()) {
                    this.differenceData.push(
                        {
                            Date: this.mutableData[1].Data[index1].Date,
                            Value0: index0 == 0 ? 0 : this.mutableData[0].Data[list0Done() ? this.mutableData[0].Data.length - 1 : index0-1].Value,
                            Value1: this.mutableData[1].Data[index1].Value
                        });
                    index1++;
                }
                else { // dates are equal
                    this.differenceData.push(
                        {
                            Date: this.mutableData[0].Data[index0].Date,
                            Value0: this.mutableData[0].Data[index0].Value,
                            Value1: this.mutableData[1].Data[index1].Value
                        });
                    index1++;
                    index0++;
                }
            }
        }

        this.flattenedItems = [].concat.apply([], this.mutableDataAxis1.map((d, idx) => d.Data.map(dd => [dd, d.name])));
        this.flattenedPointItems = [].concat.apply([], this.mutablePointData.map((d, idx) => d.Data.map(dd => [dd, d.name])));
        if(this.mutableDataAxis2) {
            this.flattenedItemsAxis2 = [].concat.apply([], this.mutableDataAxis2.map(d => d.Data.map((dd, idx) => [dd, d.name])));
        }      
      
        this.drawGraph();

        setTimeout(() => this.zoomPane.call(this.zoom.transform, d3.zoomIdentity), 1);
    }

    drawGraph() {
        if (this.svg) {
            if (this.xDomain) {
                this.x = this.x.domain(this.xDomain);
            }
            else {            
                this.x = this.x.domain(d3.extent(<[TimeSeriesItem,string][]>_.concat(this.flattenedItems, this.flattenedPointItems), function (d: any) {
                    return d[0].Date;
                }));
            }

            if(this.yDomain) {
                this.y = this.y.domain(this.yDomain).nice();
            }
            else{
                this.y = this.y.domain([
                    d3.min(<TimeSeries[]>_.concat(this.mutableDataAxis1, this.mutablePointData), function (c) { return d3.min(c.Data, function (v: TimeSeriesItem) { return v.Value; }); }),
                    d3.max(<TimeSeries[]>_.concat(this.mutableDataAxis1, this.mutablePointData), function (c) { return d3.max(c.Data, function (v: TimeSeriesItem) { return v.Value; }); })
                ]).nice();
            }   

            if(this.mutableDataAxis2) {
                this.y2.domain([
                    d3.min(this.mutableDataAxis2, function (c) { return d3.min(c.Data, function (v: TimeSeriesItem) { return v.Value; }); }),
                    d3.max(this.mutableDataAxis2, function (c) { return d3.max(c.Data, function (v: TimeSeriesItem) { return v.Value; }); })
                ]).nice();
            }            
            d3.zoomIdentity.translate(0, 0).scale(1);

            this.zoomedX = this.x;

            if(this.AllowZoomY) {
                this.zoomedY = this.y;
                this.zoomedY2 = this.y2;
            }

            this.updateAxis(true);

            this.updateGraph();
            //  this.svg.selectAll("*").remove();
            return this.svg;
        }

        this.width = this.width - this.margin.left - this.margin.right;
        this.height = this.height - this.margin.top - this.margin.bottom;

        this.x = d3.scaleTime() 
            .range([0, this.width]);

        this.y = d3.scaleLinear()
            .range([this.height, 0]);
           
        if (this.yAxisSecondAxisDataFilter) {
            this.y2 = d3.scaleLinear()
                    .range([this.height, 0]);  
       
            this.y2Axis = d3.axisRight(this.y2);          

            this.area = d3.area<TimeSeriesItem>()
                .x(d => this.zoomedX(d.Date))
                .y1(d => this.zoomedY2(d.Value))
                .y0(d=>this.zoomedY2(0))
                .curve(this.interpolationMethod);                         
        }

        if(this.IncludeDifference) {
            this.differenceArea = d3.area<any>()
                .curve(this.interpolationMethod)
                .x((d) => { 
                    return this.zoomedX(d.Date); 
                })
                .y1((d) => { 
                    return this.zoomedY(d.Value0); 
                });
        }


        if(this.userColors)
            this.color = d3.scaleOrdinal(this.userColors);
        else
            this.color = d3.scaleOrdinal(["#1f77b4","#d62728", "#ffba00"]);

        this.xAxis = d3.axisBottom(this.x)
                       .tickFormat(d=>this.multiTimeFormat(d));

        this.yAxis = d3.axisLeft(this.y);

        this.line = d3.line<TimeSeriesItem>()
            .x(d => this.zoomedX(d.Date))
            .y(d => this.zoomedY(d.Value))
            .curve(this.interpolationMethod);

        this.svg = d3.select(this.el.nativeElement).append("svg")
            .attr("width", this.width + this.margin.left + this.margin.right)
            .attr("height",  this.height + this.margin.top + this.margin.bottom)
            .append("g")
            .attr("transform", "translate(" + this.margin.left + "," + this.margin.top + ")");

        this.svg.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + this.height + ")");

        this.svg.append("clipPath")
            .attr("id", `clip-${this.UniqueId}`)
            .append("rect")
            .attr("x", 0)
            .attr("y", 0)
            .attr("width", this.width)
            .attr("height", this.height);

        this.graphContainer = this.svg.append("g")
            .attr("clip-path", `url(#clip-${this.UniqueId})`)
            .append("g");

        if (this.includeHoverLine) {
            this.setupHoverLine();
        }
        this.mutableData = this.lineData.toArray();

        this.mutableDataAxis1 = this.yAxisMutableData();
        this.mutableDataAxis2 = this.yAxis2MutableData();

        this.color.domain(this.mutableData.concat(this.mutablePointData).map(d => d.name));

        this.flattenedItems = [].concat.apply([], this.mutableDataAxis1.map(d => d.Data.map((dd, idx) => [dd, d.name])));
       
        if(this.mutableDataAxis2) {
            this.flattenedItemsAxis2 = [].concat.apply([], this.mutableDataAxis2.map(d => d.Data.map((dd, idx) => [dd, d.name])));
            this.y2.domain([
                d3.min(this.mutableDataAxis2, function (c) { return d3.min(c.Data, function (v: TimeSeriesItem) { return v.Value; }); }),
                d3.max(this.mutableDataAxis2, function (c) { return d3.max(c.Data, function (v: TimeSeriesItem) { return v.Value; }); })
            ]).nice();
        }

        if(this.xDomain) {
            this.x = this.x.domain(this.xDomain); 
        }
        else {
            this.x = this.x.domain(d3.extent(<[TimeSeriesItem, string][]>_.concat(this.flattenedPointItems, this.flattenedItems), function (d: any) {
                return d[0].Date;
            }));
        }

        if (this.yDomain) {
            this.y.domain(this.yDomain).nice();
        }
        else {
            this.y.domain([
                d3.min(<TimeSeries[]>_.concat(this.mutableDataAxis1, this.mutablePointData), function (c) { return d3.min(c.Data, function (v: TimeSeriesItem) { return v.Value; }); }),
                d3.max(<TimeSeries[]>_.concat(this.mutableDataAxis1, this.mutablePointData), function (c) { return d3.max(c.Data, function (v: TimeSeriesItem) { return v.Value; }); })
            ]).nice();
        }

        this.setupZoomBehavior();
        this.drawBorder();
        this.setupLegend(this.mutableData, this.mutablePointData);
        this.setupZoomButtons();

        this.tooltip = d3.select(this.tooltipElementRef.nativeElement)
            .style("position", "absolute")
            .style("z-index", "10")
            .style("visibility", "hidden");

        this.updateGraph();

        var yAx = this.svg.append("g")
            .attr("class", "y axis")

        var yAx2;

        if (this.yAxisSecondAxisDataFilter) {
            yAx2 = this.svg.append("g")
                .attr("class", "y2 axis")
                .attr("transform", "translate( " + this.width + ", 0 )");         
        }

        if (this.yAxisTitle) {
            yAx.append("text")
                .attr("transform", "translate(0," + this.height/2 + ")rotate(-90)")
               // .attr("y", 6)
                .attr("dx", "4em")
                .attr("dy", "1.31em")
                .style("text-anchor", "end")
                .style("fill", "#000")
                .text(this.yAxisTitle);
        }

        if (this.ySecondAxisTitle) {
            yAx2.append("text")
                .attr("transform", "translate(0," + this.height/2 + ")rotate(-90)")
             //   .attr("y", 6)
                .attr("dx", "4em")
                .attr("dy", "-.31em")
                .style("text-anchor", "end")
                .style("fill", "#000")
                .text(this.ySecondAxisTitle);
        }           
    }
 
    multiTimeFormat(date) :string {
        var formatMillisecond = d3.timeFormat("%I:%M:%S.%L"),
            formatSecond = d3.timeFormat("%I:%M:%S"),
            formatMinute = d3.timeFormat("%d-%b-%Y %I:%M"),
            formatHour = d3.timeFormat("%d-%b-%Y %I %p"),
            formatDay = d3.timeFormat("%d-%b-%Y"),
            formatWeek = d3.timeFormat("%d-%b-%Y"),
            formatMonth = d3.timeFormat("%B %Y"),
            formatYear = d3.timeFormat("%Y");

        return (d3.timeSecond(date) < date ? formatMillisecond
            : d3.timeMinute(date) < date ? formatSecond
            : d3.timeHour(date) < date ? formatMinute
            : d3.timeDay(date) < date ? formatHour
            : d3.timeMonth(date) < date ? (d3.timeWeek(date) < date ? formatDay : formatWeek)
            : d3.timeYear(date) < date ? formatMonth
            : formatYear)(date);
    }    

    setupZoomBehavior() {
        this.zoom = d3.zoom()
          //  .wheelDelta( ()=>  -d3.event.deltaY * (d3.event.deltaMode ? 120 : 1) / 800 )
            .on("zoom", () => this.zoomUpdate(this.isZoomButtonUpdate))
            ; //  .scaleExtent([.5,7]);

        if(this.xExtent) {
            this.zoom.
                translateExtent([[this.x(this.xExtent[0]), 0], [Math.max(this.width, this.x(this.xExtent[1])),Infinity]])
        }
        if(this.disableWheelZoom)
            this.zoom.filter(()=>{
                return !d3.event || (!d3.event.button && !d3.event.wheelDelta);
            });

        this.zoomPane = this.svg.append("rect")
            .attr("class", "zoomPane")
            .attr("width", this.width)
            .attr("height", this.height)
            .call(this.zoom);
    }

    setupHoverLine() {
        var that = this;

        this.hoverLine = this.svg
            .on("mousemove", function (d) { that.updateHoverLine(this) })
            .on("mouseout", d => this.removeHoverLine())
            .append("g")
            .attr("class", "hoverLine")
            .append("line");

    }

    // filter for the "first" y-axis. Just an inverse of the 2nd filter
    private yAxisFilter(d) {
        return this.yAxisSecondAxisDataFilter? !this.yAxisSecondAxisDataFilter(d):true;
    }

    private yAxisMutableData() {
        return this.mutableData.filter(d=>this.yAxisFilter(d));
    }
    private yAxis2MutableData() {
        if(!this.yAxisSecondAxisDataFilter) return null;

        return this.mutableData.filter(d=>this.yAxisSecondAxisDataFilter(d));
    }    

    updateHoverLine(el: any) {
        var xCoord = d3.mouse(el)[0];
        var vals = this.getValuesAtX(xCoord);

        this.svg.selectAll(".inflated.data-point")
            .attr("r", this.pointSizeR)
            .attr("stroke", undefined)
            .style("stroke-width", undefined)
            .classed("inflated",false);

        var points = this.svg.selectAll(".data-point")
            .filter(d => vals.values.find(v => v.value.Date == d[0].Date))
            .attr("r", this.pointSizeR+2)
            .attr("stroke","black")
            .style("stroke-width", "1px")
            .classed("inflated",true);

        var selectedDate = vals.values.first().value.Date;

        var hoverX = this.UseContinuousHoverLine ? this.zoomedX(selectedDate) : this.zoomedX(vals.datePos);

        this.hoverLine.attr("y1", 0)
            .attr("y2", this.height)
            .attr("x1", hoverX)
            .attr("x2", hoverX)
            .attr("opacity", 1)
            .style("stroke", "black")
            .style("stroke-width", "1px");

      //  this.tooltip.html(this.hoverLineDisplay(vals));
        var tooltipBounds = this.tooltip.node().getBoundingClientRect();

        // currently, we position the tooltip above the "highest" datapoint, and to the left of the hoverline.
        this.tooltip.style("visibility", "visible")
                    .style("top",(_(points.nodes()).map((p: any)=>p.cy.baseVal.value).min()-40) + "px")
                    .style("left", () => {
                        if(+hoverX > (this.width/2))
                            return (+hoverX + this.margin.left - tooltipBounds.width - 15) + "px";

                        return (+hoverX + this.margin.left + 15) + "px";
                    } );

        this.TooltipItemChange.emit(vals);
    }

    removeHoverLine() {
        this.tooltip.style("visibility", "hidden");
        this.hoverLine.attr("opacity", 0);

        this.svg.selectAll(".inflated.data-point")
            .attr("r", this.pointSizeR)
            .attr("stroke", undefined)            
            .style("stroke-width", undefined)
            .classed("inflated",false);
    }

    getValuesAtX(xCoord: number) {
        var curDate = this.zoomedX.invert(xCoord);
        var bisectDate = d3.bisector(function (d: TimeSeriesItem) { return d.Date; }).left;

        // line values range from the date of the TimeSeriesItem to the next item in the series.
        var lineValues = this.lineData.map((t: TimeSeries, i: number) => {
            var curIdx = bisectDate(t.Data, curDate, 1);

            var leftVal = t.Data[curIdx - 1];
            var rightVal = t.Data[curIdx];

            var val: TimeSeriesItem;
            if (!leftVal)
                val = rightVal;
            else if (!rightVal)
                val = leftVal;
            else
                val = curDate.getTime() - leftVal.Date.getTime() > rightVal.Date.getTime() - curDate.getTime() ? leftVal : rightVal;

            return { "seriesName": t.name, "value": leftVal };
        });

        var beginningOfDayDate = new Date(curDate.getFullYear(),curDate.getMonth(),curDate.getDate());
        // point values are single point in time.
        var pointValues = this.pointData.map((t: TimeSeries, i: number) => {
            var item = _(t.Data).filter(d => d.Date.getTime() == beginningOfDayDate.getTime()).first();

            if (!item)
                return undefined;

            return { "seriesName": t.name, "value": item };
        }).filter(d=>d !== undefined);

        return {"datePos": curDate, "values": lineValues.concat(pointValues)};
    }

    drawBorder() {
        var strokeOpacity = this.hideBorder ? 0 : 0.9;

        this.svg.append("g")
            .attr("class", "d3 border")
            .append("rect")
            .attr("x", this.margin.left * -1)
            .attr("y", this.margin.top * -1)
            .style("fill", "none")
            .style("stroke", "black")
            .style("stroke-width", "2px")
            .style("stroke-opacity", strokeOpacity)
            .attr("height", this.height + this.margin.top + this.margin.bottom)
            .attr("width", this.width + this.margin.left + this.margin.right);
    }

    updateGraph() {
        this.updateAxis();

        if(this.IncludeDifference) {
            this.updateDifferenceLines(this.differenceData);
        }
  
        if(this.yAxisSecondAxisDataFilter)
            this.updateLines(this.mutableDataAxis2, true);
        
        this.updateLines(this.mutableDataAxis1, false);

        if (this.includeLineDataPoints) {
            if(this.yAxisSecondAxisDataFilter)
                this.updateLinePoints(this.flattenedItemsAxis2 ,true);

            this.updateLinePoints(this.flattenedItems,false);
        }

        if (this.flattenedPointItems && this.flattenedPointItems.length>0) {
            this.updateLinePoints(this.flattenedPointItems, false);
        }
    }

    zoomUpdate(includeTransitions = false) {

        // if(this.xDomain) {
        //     var tx = d3.zoomIdentity.x,
        //         ty = d3.zoomIdentity.y;

        //     tx = Math.min(tx, 0);
        //     tx = Math.max(tx, this.width - this.zoomedX(this.xDomain[1]));
        //     d3.zoomIdentity.translate(tx, ty);
        // }
        this.updateAxis(includeTransitions);
   
        if (this.IncludeDifference) {
            this.updateExistingDifferenceLines(this.graphContainer.select(".diff-line.diff0"), true, includeTransitions);
            this.updateExistingDifferenceLines(this.graphContainer.select(".diff-line.diff1"),false,includeTransitions);
            this.updateExistingDifference(this.graphContainer.select("clipPath#clip-below-" + this.UniqueId ).select("path"), false, includeTransitions);
            this.updateExistingDifference(this.graphContainer.select("clipPath#clip-above-" + this.UniqueId).select("path"), true, includeTransitions);
        }

        if(this.yAxisSecondAxisDataFilter) {
            lines = this.graphContainer.selectAll(".gc-line.ax2");       
            this.updateExistingLines(lines, includeTransitions,true);
        }

        var lines = this.graphContainer.selectAll(".gc-line.ax1");
        this.updateExistingLines(lines, includeTransitions,false);
     

        this.updateExistingLinePoints(this.svg.selectAll(".data-point.ax1"), includeTransitions, false);

        if(this.yAxisSecondAxisDataFilter)
            this.updateExistingLinePoints(this.svg.selectAll(".data-point.ax2"), includeTransitions, true);
        // this.graphContainer.attr("transform","translate("+ (<any>d3.event).translate +")scale(" + d3.event.scale + ")");
    }

    setupZoomButtons() {
        var zoomInButton = d3.select("pm-icon-search-plus")
                                .on("click", ()=>{this.zoomClick(true)});

        var zoomOutButton = d3.select("pm-icon-search-minus")
            .on("click", () => { this.zoomClick(false) });

        var resetButton = d3.select("pm-icon-arrows")
            .on("click", () => { this.zoomClick(false,true) });            
    }

    zoomClick(isZoomIn:boolean, isZoomReset:boolean=false) {
        var currentDuration = this.transitionDuration;

        this.transitionDuration = currentDuration==0?500:currentDuration;
        this.isZoomButtonUpdate = true;

        if(isZoomReset)
            this.zoomPane.call(this.zoom.transform, d3.zoomIdentity);
        else
            this.zoomPane.call(this.zoom.scaleBy, isZoomIn ? 2 : 0.5);

        this.isZoomButtonUpdate = false;         
        this.transitionDuration = currentDuration;
    }

 

    setupLegend(mutableData: TimeSeries[], mutablePointData: TimeSeries[]) {
        var numberOfLines = mutableData.length;
        
        var legendContainer = this.svg.append("g");
        var legend = legendContainer
            .attr("font-size", 12)
            .attr("text-anchor", "end")
            .selectAll("g")
            .data(mutableData.concat(mutablePointData))
            .enter().append("g")
            .attr("transform", function (d, i) { return "translate(0," + i * 20 + ")"; });

        legend.filter((d:any,i:number)=> i < numberOfLines )
              .append("line")
                    .attr("x1", this.width - 19)
                    .attr("x2", this.width)
                    .attr("y1", 19 / 2)
                    .attr("y2", 19 / 2)
                    .style('stroke-dasharray', (d: any, i: number) => i == 0 ? undefined : `${i * 8},${i * 8}`)
                    .style("stroke-width", 3)
                    .style("stroke", d => { 
                        if(this.yAxisSecondAxisDataFilter && this.yAxisSecondAxisDataFilter(d))
                            return "lightgray";
                        return this.color(d.name);
                    });

        legend.filter((d: any, i: number) => i >= numberOfLines)
            .append("circle")
            .attr("r", 4)
            .attr("cx", this.width - 15)
            .attr("cy", 19 / 2)
            .style("fill", d => { 
                return this.color(d.name);
            });                    

        legend.append("text")
            .attr("x", this.width - 24)
            .attr("y", 9.5)
            .attr("dy", "0.32em")
            .text(function (d) { return d.name; });

        var legendPadding = 5;
        legendContainer.insert("rect","g")
            .attr("x", legendContainer.node().getBBox().x - legendPadding)
            .attr("y", legendContainer.node().getBBox().y)
            .style("stroke-width", "1")
            .style("stroke", "black")
            .style("fill", "white")
            .style("fill-opacity", 0.8)
            .attr("width", legendContainer.node().getBBox().width + (legendPadding*2))
            .attr("height", legendContainer.node().getBBox().height + legendPadding);
    }

    updateAxis(includeTransitions: boolean = true) {
        var xAx = this.svg.select(".x.axis");

        if (includeTransitions && this.transitionDuration > 0)
            xAx = xAx.transition()
                .duration(this.transitionDuration);

        if (d3.event != null && d3.event.transform && this.AllowZoomX) {
            this.zoomedX = d3.event.transform.rescaleX(this.x);
        }
        else {
            this.zoomedX = this.zoomedX ? this.zoomedX : this.x;
        }

        var rescaledXAxis = this.xAxis.scale(this.zoomedX)
        xAx.call(rescaledXAxis)
            .selectAll("text")
            .style("text-anchor", "end")
            .attr("dx", "-.3em")
            .attr("dy", ".5em")
            .attr("transform", "rotate(" + this.xAxisTextRotation + ")");

        var yAx = this.svg.select(".y.axis");

        if (includeTransitions && this.transitionDuration > 0)
            yAx = yAx.transition()
                .duration(this.transitionDuration);


        if (d3.event != null && d3.event.transform  && this.AllowZoomY) {
            this.zoomedY = d3.event.transform.rescaleY(this.y);
        }
        else {
            this.zoomedY = this.zoomedY ? this.zoomedY : this.y;
        }
        var rescaledYAxis = this.yAxis.scale(this.zoomedY);
        yAx.call(rescaledYAxis);

        if (this.yAxisSecondAxisDataFilter) {
            var yAx2 = this.svg.select(".y2.axis");

            if (includeTransitions && this.transitionDuration > 0)
                yAx2 = yAx2.transition()
                    .duration(this.transitionDuration);

            if (d3.event != null && d3.event.transform && this.AllowZoomY) {
                this.zoomedY2 = d3.event.transform.rescaleY(this.y2);
            }
            else {
                this.zoomedY2 = this.zoomedY2 ? this.zoomedY2 : this.y2;
            }
            var rescaledY2Axis = this.y2Axis.scale(this.zoomedY2);
            yAx2.call(rescaledY2Axis);
        }
    }

    updateDifferenceLines(differenceData: any) {
        var y =   this.zoomedY;

        var axClass =   "ax1";

        var enteredClipsBelow = this.graphContainer.selectAll(`.clip-below-${this.UniqueId}`).data([differenceData])
            .enter()
            .append("clipPath")
            .attr("id", `clip-below-${this.UniqueId}`);

        enteredClipsBelow.append("path")
            .call(this.zoom);

        // enteredClipsBelow.merge(enteredClipsBelow)
        //         .attr("d", d=>this.differenceArea.y0(this.height)(d.Data));

        var enteredClipsAbove = this.graphContainer.selectAll(`.clip-above-${this.UniqueId}`).data([differenceData])
            .enter()
            .append("clipPath")
            .attr("id", `clip-above-${this.UniqueId}`);

        enteredClipsAbove.append("path")
            .call(this.zoom);

        // enteredClipsAbove.merge(enteredClipsAbove)

        this.updateExistingDifference(enteredClipsBelow.merge(enteredClipsBelow).select("path"), false,true);
        this.updateExistingDifference(enteredClipsAbove.merge(enteredClipsAbove).select("path"), true, true);

        // var enteredDiffAbove = this.graphContainer.selectAll(".area.above")
        //     .data([mutableData[0]])
        //         .enter()
        //     .append("path")
        //     .attr("class", "area above")
        //     .attr("clip-path", "url(#clip-above)");

        // enteredDiffAbove.merge(enteredDiffAbove)
        //     .attr("d", d=>this.differenceArea.y0(function (d) { return y(d.Value); })(d.Data));

        // var enteredDiffBelow = this.graphContainer.selectAll(".area.below")
        //     .data([mutableData[1]])
        //         .enter()
        //     .append("path")
        //     .attr("class", "area below")
        //     .attr("clip-path", "url(#clip-below)");

        // enteredDiffBelow.merge(enteredDiffBelow)                
        //     .attr("d", d=> this.differenceArea(d.Data));                

        var line0 = this.graphContainer.selectAll(`.diff-line.diff0.${axClass}`)
            .data([differenceData])
            .enter()
            .append("path")
                .style('opacity', 0)
                .attr("class", `diff-line ${axClass} diff0`)
                .call(this.zoom);       

        var line1 = this.graphContainer.selectAll(`.diff-line.diff1.${axClass}`)
            .data([differenceData])
            .enter()
            .append("path") 
                .style('opacity', 0)
                .attr("class", `diff-line ${axClass} diff1`)                
                .call(this.zoom);            
 

        this.updateExistingDifferenceLines(line0.merge(line0), false, true);
        this.updateExistingDifferenceLines(line1.merge(line1), true, true);

        line0.exit()
            .remove();

        line1.exit()
            .remove();
    }
    updateExistingDifferenceLines(lines: any, isAbove: boolean, includeTransitions:boolean) {
        var that = this;

        if (includeTransitions && this.transitionDuration > 0) 
            lines = lines.transition().duration(this.transitionDuration);

        lines = lines
            .attr("d", isAbove ? this.differenceArea.y0(d => { return this.zoomedY(d.Value1); }) : this.differenceArea)
            .style('opacity', 1)
            .style("fill", isAbove ? "lightsalmon" : "lightgreen" )
            .attr("clip-path", isAbove ? `url(#clip-above-${this.UniqueId})` :  `url(#clip-below-${this.UniqueId})`);

    }
    updateExistingLines(lines: any, includeTransitions: boolean, isYAxis2 :boolean) {
        var that = this;
        var shape = isYAxis2? this.area:this.line;

        if (includeTransitions && this.transitionDuration > 0) {
            lines = lines.transition().duration(this.transitionDuration);

            if(this.useTweenTransition)
                lines.attrTween("d", function (d) { return that.pathTween(shape(d.Data), 4, this)() });
            else {
                lines.attr("d", d => shape(d.Data));
            }
        }
        else {
            lines.attr("d", d => shape(d.Data));
        }

        lines = lines
            .style('opacity', 1)
            .style('stroke-width', this.lineSizePx)
            .style("stroke", d => this.color(d.name));     
    }

    updateLines(mutableData: TimeSeries[], isYAxis2 :boolean) {
        var y = isYAxis2? this.zoomedY2 : this.zoomedY;

        var axClass = isYAxis2?"ax2":"ax1";

        var gLines = this.graphContainer.selectAll(`.chart-line.${axClass}`)
            .data(mutableData);

        var enteredGLines = gLines.enter()
            .append("g")
            .attr("class", `chart-line ${axClass}`)
            .call(this.zoom);

        var enteredLines = enteredGLines
            .append("path")
            .style('opacity', 0)
            .style('stroke-dasharray', (d: any, i: number) => i == 0 ? undefined : `${i * 8},${i * 8}`)
            .attr("class", `gc-line ${axClass}`);

        this.updateExistingLines(enteredGLines.merge(gLines).select(".gc-line"), true,isYAxis2);

        gLines.exit()
            .remove();
    }

    updateExistingDifference(clip, isAbove : boolean, includeTransitions:boolean) {
        if (includeTransitions && this.transitionDuration > 0) 
            clip = clip.transition().duration(this.transitionDuration);

        if(isAbove) {
            clip.attr("d", this.differenceArea.y0(0));
        }
        else {
            clip.attr("d", this.differenceArea.y0(this.height));
        }
    }

    updateExistingLinePoints(circles, includeTransitions: boolean, isYAxis2 :boolean) {
        var y = isYAxis2? this.zoomedY2 : this.zoomedY;
    
        if (includeTransitions && this.transitionDuration > 0)
            circles = circles.style('opacity', 1)
                .transition().duration(this.transitionDuration);

        circles.style('opacity', 1)
            .style('fill-opacity', .8)
            .attr("cx", (d: [TimeSeriesItem, string]) => this.zoomedX(d[0].Date))
            .attr("cy", (d: [TimeSeriesItem, string]) => y(d[0].Value));
    }

    updateLinePoints(dataPoints: Array<[TimeSeriesItem, string]>, isYAxis2 :boolean) {
        var y = isYAxis2? this.zoomedY2 : this.zoomedY;
        var axClass = isYAxis2?"ax2":"ax1";

        var circles = this.graphContainer.selectAll(`.data-point.${axClass}`)
            .data(dataPoints, (d: [TimeSeriesItem, string]) => d[0].Date);

        var enteredCircles = circles.enter().append("circle")
            .attr("r", this.pointSizeR)
            .style("fill", d => isYAxis2? "lightgray": this.color(d[1]))
            .style('opacity', 0)
            .attr("class", `data-point ${axClass}`)
            //   .attr("stroke", "black")
            .attr("cx", (d: [TimeSeriesItem, string]) => this.zoomedX(d[0].Date))
            .attr("cy", (d: [TimeSeriesItem, string]) => y(d[0].Value))
            .call(this.zoom);

        circles.exit()
            .remove();

        this.updateExistingLinePoints(enteredCircles.merge(circles), true, isYAxis2);
    }

    pathTween(d1, precision, element) {
        return function () {
            if(!d1) return "";
            var path0 = element,
                path1 = path0.cloneNode(),
                n0 = path0.getTotalLength(),
                n1 = (path1.setAttribute("d", d1), path1).getTotalLength();

            // Uniform sampling of distance based on specified precision.
            var distances = [0], i = 0, dt = precision / Math.max(n0, n1);
            while ((i += dt) < 1) distances.push(i);
            distances.push(1);

            // Compute point-interpolators at each distance.
            var points = distances.map(function (t) {
                var p0 = path0.getPointAtLength(t * n0),
                    p1 = path1.getPointAtLength(t * n1);
                return d3.interpolate([p0.x, p0.y], [p1.x, p1.y]);
            });

            return function (t) {
                return t < 1 ? "M" + points.map(function (p) { return p(t); }).join("L") : d1;
            };
        };
    }

}