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

graph.edge("WAITING","↑", label='TURN 90')
graph.edge("WAITING","↓", label='TURN 180')
graph.edge("WAITING","←", label='TURN 270')
graph.edge("WAITING","→", label='TURN 360')

graph.edge("↑","PIT STOP", label='  ε  ')
graph.edge("↓","PIT STOP", label='  ε  ')
graph.edge("←","PIT STOP", label='  ε  ')
graph.edge("→","PIT STOP", label='  ε  ')

graph.edge("PIT STOP","WAITING", label='ε')

graph.edge("WAITING","WAITING", label='MOVE X')




graph.view()