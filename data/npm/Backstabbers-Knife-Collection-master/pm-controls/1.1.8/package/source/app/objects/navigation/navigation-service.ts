import { ApplicationRef, 
         ComponentFactoryResolver, 
         ComponentRef, 
         Injectable,
         Injector, 
         ViewContainerRef, 
         EmbeddedViewRef, 
         Type }                     from '@angular/core';
import { NavigationItem } from '../../objects/navigation/navigation-item';
import { Dictionary } from '../../objects/dictionary';

@Injectable()
export class NavigationService {
    public Items: Dictionary<NavigationItem>;    
}