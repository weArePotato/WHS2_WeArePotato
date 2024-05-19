import React, { Component } from 'react'
import { connect } from 'react-redux'
import _ from 'lodash'
import Heading from 'grommet/components/Heading'

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
      <Heading tag="h1">{this.state.sampleData}</Heading>
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