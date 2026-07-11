from langgraph.graph import (
    StateGraph,
    END
)

from models.graph_state import (
    GraphState
)

from graph.nodes.router_agent import (
    RouterAgent
)

from graph.nodes.retrieval_agent import (
    RetrievalAgent
)


def build_graph():

    graph = StateGraph(
        GraphState
    )

    graph.add_node(
        "router",
        RouterAgent()
    )

    graph.add_node(
        "retrieval",
        RetrievalAgent()
    )

    graph.set_entry_point(
        "router"
    )

    graph.add_edge(
        "router",
        "retrieval"
    )

    graph.add_edge(
        "retrieval",
        END
    )

    return graph.compile()