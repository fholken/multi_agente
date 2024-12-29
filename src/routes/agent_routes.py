from fastapi import APIRouter

from ..services.multiagent import graph

router = APIRouter(prefix="/agent")

@router.get("/multiagent")
async def get_all_agents():
    return graph.invoke({"my_var": "World", "customer_name": "John"})