## usage
```html
<a  modal-box  (optional-attributes)>
	<sapn>The button label</sapn>
	<modal-box-header>
		//modal header content
	</modal-box-header>
	<modal-box-content>
		//modal body content
	</modal-box-content>
</a>
```

### optional-attributes
```close-option="false"``` // disable close button (default enable).

```open="true"``` // open _modal-box_ without user interaction (default `false`).

```close=" (variable) "``` // close _modal-box_ **function** (optional). then use ```variable()``` in parent component to close the _modal-box_.

```perfect-scrollbar="true"``` // enable the perfect-scrollbar inner container (default false).

### close from outside
emit ```modalBoxClose``` event (or use the _close attribute option_)
