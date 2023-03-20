# sourcery skip: assign-if-exp, swap-if-expression
import os
import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = False

parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "frontend/build")
# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    # component = components.declare_component("circle_packing_chart", path=build_dir)

    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("circle_packing_chart"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "circle_packing_chart",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    _component_func = components.declare_component("circle_packing_chart", path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def circle_packing_chart(name, key=None):
    """Create a new instance of "circle_packing_chart".

    Parameters
    ----------
    name: str
        The name of the thing we're saying hello to. The component will display
        the text "Hello, {name}!"
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    int
        The number of times the component's "Click Me" button has been clicked.
        (This is the value passed to `Streamlit.setComponentValue` on the
        frontend.)

    """
    return _component_func(name=name, key=key, default=0)


# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run circle_packing_chart/__init__.py`
if not _RELEASE:
    import streamlit as st
    import pickle
    with open('/home/shubhrajg/Documents/circle_packing_component/component-template/template/circle_packing_chart/for_circle_packing_movie.pkl', 'rb') as file:
        dict_new = pickle.load(file)

    data11 = {'id': 'Main', 'children': []}
    for k,v in dict_new.items():
        # print(k)
        for i,j in v.items():
            # print(i)
            for k in j:
                k['id'] = str(k['id'])

                # k['children'] = None
                # for l,m in k.items():

                #     if l == 'children':
                #         for n in m:
                #             n['datum'] = n['datum'] + 1
                            # print(n)
    data11['children'].extend(dict_new['63655e5a93cdbe5d7df1f69d']['101192959421944_140161578850356'][:5])
    # d1={}
    # for i in dict_new['63655e5a93cdbe5d7df1f69d']['101192959421944_140161578850356'][:10]:
    #     d1 |= i
    # print('\n', d1)
    # print('\n', dict_new['63655e5a93cdbe5d7df1f69d']['101192959421944_140161578850356'][:2])
    st.subheader("Component with constant args")
    test = {
      "id": "Main",
      "color": "hsl(266, 70%, 50%)",
      "children": [
        {
          "id": "-1",
          "color": "hsl(50, 70%, 50%)",
          "children": [
            {
              "id": "cchart",
              "color": "hsl(83, 70%, 50%)",
              "datum": 0.12
            },
            {
              "id": "xAxis",
              "color": "hsl(59, 70%, 50%)",
              "datum": 0.13
            },
            {
              "id": "yAxis",
              "color": "hsl(42, 70%, 50%)",
              "datum": 0.14
            },
            {
              "id": "layers",
              "color": "hsl(53, 70%, 50%)",
              "datum": 0.56
            }
          ]
        },
        {
      "id": "0",
      "color": "hsl(69, 70%, 50%)",
      "children": [
        {
          "id": "randomize",
          "color": "hsl(241, 70%, 50%)",
          "datum": 0.5
        },
        {
          "id": "resetClock",
          "color": "hsl(190, 70%, 50%)",
          "datum": 0.10
        },
        {
          "id": "noop",
          "color": "hsl(84, 70%, 50%)",
          "datum": 0.20
        },
        {
          "id": "tick",
          "color": "hsl(293, 70%, 50%)",
          "datum": 0.24
        },
        {
          "id": "forceGC",
          "color": "hsl(351, 70%, 50%)",
          "datum": 0.31
        },
        {
          "id": "stackTrace",
          "color": "hsl(103, 70%, 50%)",
          "datum": 0.17
        },
        {
          "id": "dbg",
          "color": "hsl(160, 70%, 50%)",
          "datum": 0.9
        }
      ]
    }
     ]
    }
    # print(test)
    circle_packing_chart(data11, key="foo")
