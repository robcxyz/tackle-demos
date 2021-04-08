# tackle-demo

Simple demo to introduce the format and features for [`tackle-box`](https://github.com/geometry-labs/tackle-box)

```
pip3 install tackle-box 
tackle https://github.com/robcxyz/tackle-demo
```

This demo walks you through many of the aspects of tackle boxes DSL. 

```shell
? What demos do you want to do?  (<up>, <down> to move, <space> to select, <a> to toggle, <i> to invert)
 ❯○ Monty Python basic demo
  ○ Embedded tackle boxes
  ○ A tutorial of all the hooks and providers
  ○ A tutorial on useful patterns with jinja
  ○ Galllery of the most popular cookiecutters
```

### Basic Demo 

Simply write your tackle box per this format. The key in the jinja syntax defaults to the context filename for the template, in this case `yaml`.

A `tackle.yaml` file placed in a directory and run with `tackle .` would call the script.
```yaml
---
name:
  type: input
  message: What is your name?

colors:
  type: checkbox
  message: What are your favorite colors?
  choices:
    - blue
    - green
    - grey

wingspeed:
  type: select
  message: What is the airspeed velocity of an unladen swallow??
  choices:
    - I donno
    - What do you mean? African or European swallow?

bad_outcome:
  type: print
  statement: Wrong answer {{ name }}... (Flung off bridge)
  when: "{{ 'I donno' in wingspeed }}"

color_essays:
  type: input
  message: Please tell me how much you like the color {{item}}?
  default: Oh color {{item}}, you are so frickin cool...
  loop: "{{ colors }}"
  when: "{{ colors|length > 0 }}"
```
