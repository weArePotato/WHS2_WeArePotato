import { 
  Component, 
  Input, 
  EventEmitter, 
  Output }                from '@angular/core';
import { BreadcrumbPath } from '../../../controls/components/breadcrumb/breadcrumb-path';

@Component({
  selector: 'pm-breadcrumb',
  //templateUrl: './app/controls/components/breadcrumb/breadcrumb.html',
  templateUrl: './breadcrumb.html'
})
export class BreadcrumbComponent {
  @Output() Click = new EventEmitter();
  private path: string;

  @Input() 
  set Path(value: string) {
    this.path = value;

    var paths = this.path.split("/");
    var crumbs = [];
    var fullPath = '';
    for (var i = 0; i < paths.length; i++) {
      var path = paths[i];
      if (!path) continue;
      fullPath += path + "/";
      var breadcrumb = new BreadcrumbPath();

      breadcrumb.FullPath = fullPath;
      breadcrumb.Path = path;
      
      crumbs.push(breadcrumb);
    }

    this.Items = crumbs;
  }

  get Path(): string {
    return this.path;
  }

  Items: Array<BreadcrumbPath> = [];

  OnLinkClick(path: BreadcrumbPath) {
    this.Click.emit(path);
  }
}