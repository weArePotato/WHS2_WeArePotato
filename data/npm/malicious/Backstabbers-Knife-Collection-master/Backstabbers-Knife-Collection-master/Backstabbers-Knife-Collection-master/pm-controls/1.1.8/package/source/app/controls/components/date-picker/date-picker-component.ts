import { 
  Component, 
  ChangeDetectionStrategy,
  ChangeDetectorRef,
  ViewContainerRef,
  forwardRef, EventEmitter,
  OnInit, Input, 
  Output,
  OnDestroy
} from '@angular/core'; 

import { 
  NG_VALUE_ACCESSOR, 
  ControlValueAccessor
} from '@angular/forms';

import * as moment_            from 'moment';

const moment: any = (<any>moment_).default || moment_;

export declare interface CalendarDate {
  day: number;
  month: number;
  year: number;
  enabled: boolean;
  today: boolean;
  selected: boolean;
}

export const CALENDAR_VALUE_ACCESSOR: any = {
  provide: NG_VALUE_ACCESSOR,
  useExisting: forwardRef(() => DatePickerComponent),
  multi: true
};

@Component({  
  selector: 'pm-date-picker',
  //templateUrl: './app/controls/components/date-picker/date-picker.html',
  templateUrl: './date-picker.html',
  changeDetection: ChangeDetectionStrategy.OnPush,
  providers: [CALENDAR_VALUE_ACCESSOR]
})
export class DatePickerComponent implements ControlValueAccessor, OnInit, OnDestroy {

  constructor(
    public changeDetectorRef: ChangeDetectorRef,
    viewContainerRef: ViewContainerRef) {
    this.changeDetectorRef.detach();
    this.el = viewContainerRef.element.nativeElement;
    this.clickEvent = this.HandleClick.bind(this);
  }

  @Input() Format: string;
  @Input() firstWeekdaySunday: boolean;
  @Input() ShowTooltip: boolean;
  @Input() TooltipContent: string;
  @Input() Label;
  @Input() Watermark: string;
  @Input() Value: any;
  @Output() ValueChange: EventEmitter<any> = new EventEmitter<any>();
  @Input() IsDisabled: boolean;
  @Input() IsDateTime: boolean;
  @Output() TextChange: EventEmitter<string> = new EventEmitter<string>();

  private isDropDownOpen: boolean;
  @Input()
  get IsDropDownOpen() : boolean 
  {
    return this.isDropDownOpen;
  }

  set IsDropDownOpen(value: boolean) {
    this.isDropDownOpen = value;
    this.changeDetectorRef.detectChanges();
  }

  private text: string;
  @Input()
  get Text() : string 
  {
    return this.text;
  }

  set Text(value: string) {
    this.text = value;
    this.TextChange.emit(value);
    this.changeDetectorRef.detectChanges();
  }

  public date: any = moment();
  private onChange: Function;
  private onTouched: Function;
  private el: Element;
  public days: CalendarDate[] = [];
  public weeks: any[];
  private clickEvent;
  private onTouchedCallback: () => void = () => { };

  SetValue(value: any) {
    let date = (value instanceof moment) ? value : moment(value, this.Format);
    this.Value = date.format(this.Format);
    this.ValueChange.emit(this.Value);
    this.Text = this.Value;
  }

  ngOnInit() {
    this.IsDropDownOpen = this.IsDropDownOpen || false;    
    this.Format = this.Format || 'DD-MMM-YYYY';
    this.TooltipContent = "Date format is " + this.Format;
    this.firstWeekdaySunday = this.firstWeekdaySunday || false; 
    
    setTimeout(() => {
      if (this.Value) {
      //   let value = moment();
        this.Text = this.Value;
        this.changeDetectorRef.detectChanges();
      }
      this.generateCalendar();
    });

    let body = document.querySelector('body');
    body.addEventListener('click', this.clickEvent, false);
    this.changeDetectorRef.detectChanges();
  }

  ngOnDestroy() {
    let body = document.querySelector('body');
    body.removeEventListener('click', this.clickEvent, false);
  }

  HandleClick(e) {
    if (!this.IsDropDownOpen || !e.target) { return; };
    if (this.el !== e.target && !this.el.contains((<any>e.target))) {
      this.close();
    }    
  }

  onTextChange(newValue) {
    let date = moment(newValue, this.Format, true);
    if (date.isValid())
    {
      this.Value = date.format(this.Format);
      this.ValueChange.emit(this.Value);  
      this.date = date;
      this.ShowTooltip = false;
      this.generateCalendar();
    }
    else
    {
      this.Value = undefined;
      this.ShowTooltip = true;
    }
    this.Text = newValue;
    this.ValueChange.emit(this.Value);
  }

  onBlurChange(value) {
    this.ShowTooltip = false;
  }

  onFocusChange(value) {
    if (this.Value == undefined)
      this.ShowTooltip = true;
  }

  generateCalendar() {
    let date = moment(this.date);
    let month = date.month();
    let year = date.year();
    let n: number = 1;
    let firstWeekDay: number = (this.firstWeekdaySunday) ? date.date(2).day() : date.date(1).day();

    if (firstWeekDay !== 1) {
      n -= (firstWeekDay + 6) % 7;
    }

    this.days = [];
    
    let selectedDate = moment(this.Value, this.Format);
    for (let i = n; i <= date.endOf('month').date(); i += 1) {
      let currentDate = moment(`${i}.${month + 1}.${year}`, 'DD.MM.YYYY');
      let today = (moment().isSame(currentDate, 'day') && moment().isSame(currentDate, 'month')) ? true : false;
      let selected = (selectedDate.isSame(currentDate, 'day')) ? true : false; 

      if (i > 0) {
        this.days.push({ 
          day: i,
          month: month + 1,
          year: year,
          enabled: true,
          today: today,
          selected: selected
        });
      } else {
        this.days.push({ 
          day: null,
          month: null,
          year: null,
          enabled:false,
          today: false,
          selected: false 
        });
      }
    }

    this.weeks = [];
    var chunkSize = 7;
    for (let i=0; i < this.days.length; i += chunkSize)
      this.weeks.push(this.days.slice(i, i+chunkSize));
  }

  selectDate(e: MouseEvent, d: CalendarDate) {
    e.preventDefault();

    let date: CalendarDate = d;
    let selectedDate = moment(`${date.day}.${date.month}.${date.year}`, 'DD.MM.YYYY');
    this.SetValue(selectedDate);
    this.close();
    this.generateCalendar();
  }

  prevMonth() {
    this.date = this.date.subtract(1, 'month');
    this.generateCalendar();
    this.changeDetectorRef.detectChanges();
  }

  nextMonth() {
    this.date = this.date.add(1, 'month');
    this.generateCalendar();
    this.changeDetectorRef.detectChanges();
  }

  writeValue(value: any) {
    this.Value = value;
  }

  registerOnChange(fn: any) {
    this.ValueChange = fn;
  }

  registerOnTouched(fn: any) {
    this.onTouchedCallback = fn;
  }

  open() {
    this.IsDropDownOpen = true;
  }

  close() {
    this.IsDropDownOpen = false;
  }
}