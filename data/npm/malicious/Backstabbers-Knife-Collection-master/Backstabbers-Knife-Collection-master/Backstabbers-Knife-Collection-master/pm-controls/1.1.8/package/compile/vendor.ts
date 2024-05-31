

// Angular 5
import '@angular/platform-browser';
import '@angular/platform-browser-dynamic';
import '@angular/core';
import '@angular/common';
import '@angular/common/http';
import '@angular/router';
import '@angular/forms';

// RxJS
import 'rxjs';

//d3
import '../source/bundles/d3-bundle';

import 'lodash';
import 'immutable';

// moment
import 'moment';

import 'file-saver';

import { enableProdMode } from '@angular/core';

if (process.env.ENV === 'production') {
// Production
    enableProdMode();
} else {
// Development
}