import React, { Component } from 'react'
import { connect } from 'react-redux'
import _ from 'lodash'

import {reduxActions} from '../../redux-modules'

export class SampleComponent extends Component {
  constructor(props) {
    super(props)
    this.state = props
  }

  handleStateChange() {
    const reduxState = store.getState()
    this.setState(_.defaultsDeep(mapStateToProps(reduxState), this.state))
  }

  componentDidMount() {
    this.unsubscribe = store.subscribe(this.handleStateChange.bind(this))
  }

  componentWillUnmount() {
    this.unsubscribe()
  }

  render() {
    return (
      <div>{this.state.sampleData}</div>
    )
  }
}

const mapStateToProps = (state) => {
  return {
    ...state.SampleReducer
  }
}

const mapDispatchToProps = (dispatch) => {
  return { dispatch }
}

export default connect(mapStateToProps, mapDispatchToProps)(SampleComponent)
