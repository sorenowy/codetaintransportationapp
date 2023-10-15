from fastapi import APIRouter, Path, status
from app.api.v1.schema.schema import ResponseSchema
from app.service.route_service import RouteService
from app.model.route import RouteRequestDTO

route_router = APIRouter(prefix="/routes", tags=["Routes"])


@route_router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_routes():
    result = await RouteService.get_all_routes()
    return ResponseSchema(detail="SUCCESS", result=result)


@route_router.get("/{routeId}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_route_by_id(routeId: int):
    result = await RouteService.get_route_by_id(routeId)
    return ResponseSchema(detail="SUCCESS", result=result)


@route_router.post(
    "",
    response_model=ResponseSchema,
    response_model_exclude_none=True,
    status_code=status.HTTP_200_OK
)
async def create_route(route_data: RouteRequestDTO):
    await RouteService.create_route(route_data)
    return ResponseSchema(detail="SUCCESS")

@route_router.post("/{routeId}/select", response_model=ResponseSchema, response_model_exclude_none=True)
async def select_route(routeId: int):
    await RouteService.select_route(routeId)
    return ResponseSchema(detail="SUCCESS", result="Email has been sent to user.")


@route_router.delete("/{routeId}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_route(routeId: int):
    await RouteService.delete_route(routeId)
    return ResponseSchema(detail="SUCCESS")


@route_router.patch("/{routeId}", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_route(route_data: RouteRequestDTO, routeId: int):
    await RouteService.update_route(routeId, route_data)
    return ResponseSchema(detail="SUCCESS")