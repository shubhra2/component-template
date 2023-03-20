import {
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode, useState } from "react"
import { ResponsiveCirclePacking } from '@nivo/circle-packing'
// interface State {
//   numClicks: number
//   isFocused: boolean
// }

/**
 * This is a React-based component template. The `render()` function is called
 * automatically when your component should be re-rendered.
 */

function MyChart({ data }: {data: any}) {
  const [zoomedId, setZoomedId] = useState<string | null>(null)
  return (
      <ResponsiveCirclePacking
          data={data}
          margin={{ top: 20, right: 20, bottom: 20, left: 20 }}
          id="id"
          value="datum"
          // valueFormat=">-.2f"
          colors={{ scheme: 'nivo' }}
          childColor={{ theme: 'background' }}
          padding={10}
          enableLabels={true}
          labelsFilter={function(n){return 2===n.node.depth}}
          labelsSkipRadius={40}
          labelTextColor={{ theme: 'labels.text.fill' }}
          borderWidth={1}
          borderColor={{ theme: 'labels.text.fill' }}
          zoomedId={zoomedId}
          motionConfig="slow"
          onClick={node => {
              setZoomedId(zoomedId === node.id ? null : node.id)
          }}


      />
  )
}
class MyComponent extends StreamlitComponentBase {
  // public state = { numClicks: 0, isFocused: false }

  public render = (): ReactNode => {
    // Arguments that are passed to the plugin in Python are accessible
    // via `this.props.args`. Here, we access the "name" arg.
    
  

    // Streamlit sends us a theme object via props that we can use to ensure
    // that our component has visuals that match the active theme in a
    // streamlit app.
    // const { theme } = this.props
    // const style: React.CSSProperties = {}
    const data1 = this.props.args['name']
    // console.log(data1)
    // Maintain compatibility with older versions of Streamlit that don't send
    // a theme object.
    // if (theme) {
    //   // Use the theme object to style our button border. Alternatively, the
    //   // theme style is defined in CSS vars.
    //   const borderStyling = `1px solid ${
    //     this.state.isFocused ? theme.primaryColor : "gray"
    //   }`
    //   style.border = borderStyling
    //   style.outline = borderStyling
    // }

    // Show a button and some text.
    // When the button is clicked, we'll increment our "numClicks" state
    // variable, and send its new value back to Streamlit, where it'll
    // be available to the Python program.
    return (
      <div style={{height: '800px'}}>
        <MyChart data={data1}></MyChart>
      </div>
    )
  }
}

// "withStreamlitConnection" is a wrapper function. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
export default withStreamlitConnection(MyComponent)
