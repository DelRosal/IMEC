import graphviz

#CREATE GRAPH
graph=graphviz.Digraph('G', filename='Graph')
  
#LEFT TO RIGHT
graph.attr(rankdir='LR')
  
#SHAPE
graph.attr('node', shape="doublecircle")
graph.node("WAITING")

graph.attr('node', shape='circle')
  
#EDGES

graph.edge("","WAITING")


graph.edge("WAITING","↑", label='TURN 90')
graph.edge("WAITING","↓", label='TURN 180')
graph.edge("WAITING","←", label='TURN 270')
graph.edge("WAITING","→", label='TURN 360')

graph.edge("WAITING","MOVE", label='MOV X')
graph.edge("MOVE","WAITING", label='  ε  ')

graph.edge("↑","PIT STOP", label='  ε  ')
graph.edge("↓","PIT STOP", label='  ε  ')
graph.edge("←","PIT STOP", label='  ε  ')
graph.edge("→","PIT STOP", label='  ε  ')

graph.edge("PIT STOP","WAITING", label='ε')



graph.view()
