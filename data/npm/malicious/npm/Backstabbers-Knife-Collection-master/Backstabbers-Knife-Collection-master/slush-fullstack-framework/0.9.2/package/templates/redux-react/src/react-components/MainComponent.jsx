import React, { Component } from 'react'
import { Provider as StoreProvider } from 'react-redux'
import '../redux-modules'
import SampleComponent from './sample/SampleComponent.jsx'

export class MainComponent extends Component {

  constructor(props) {
    super(props)
    this.state = props
  }

  render() {
    return (
      <StoreProvider store={window.store}>
        <SampleComponent></SampleComponent>
      </StoreProvider>
    )
  }
}

export default MainComponent
