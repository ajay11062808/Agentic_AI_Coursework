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

from graph.nodes.cis_retrieval_agent import (
    CISRetrievalAgent
)

from graph.nodes.nist_retrieval_agent import (
    NISTRetrievalAgent
)

from graph.nodes.gdpr_retrieval_agent import (
    GDPRRetrievalAgent
)

from graph.nodes.analysis_agent import (
    AnalysisAgent
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
        "cis",
        CISRetrievalAgent()
    )

    graph.add_node(
        "nist",
        NISTRetrievalAgent()
    )

    graph.add_node(
        "gdpr",
        GDPRRetrievalAgent()
    )

    graph.add_node(
        "analysis",
        AnalysisAgent()
    )

    graph.set_entry_point(
        "router"
    )

    graph.add_edge(
        "router",
        "cis"
    )

    graph.add_edge(
        "router",
        "nist"
    )

    graph.add_edge(
        "router",
        "gdpr"
    )

    graph.add_edge(
        "cis",
        "analysis"
    )

    graph.add_edge(
        "nist",
        "analysis"
    )

    graph.add_edge(
        "gdpr",
        "analysis"
    )

    graph.add_edge(
        "analysis",
        END
    )

    return graph.compile()