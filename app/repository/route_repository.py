from app.database.config.connection import prisma_connection
from app.model.route import Route, RouteRequestDTO

class RouteRepository:
    
    @staticmethod
    async def get_all_routes():
        return await prisma_connection.prisma.route.find_many()
    
    @staticmethod
    async def create_route(route: RouteRequestDTO):
        return await prisma_connection.prisma.route.create({
            "start_location": route.start_location,
            "end_location": route.end_location,
            "price_per_km": route.price_per_km,
            "distance": route.distance,
            "date_of_execution": route.date_of_execution
        })
        
    @staticmethod
    async def get_route_by_id(id: int):
        return await prisma_connection.prisma.route.find_first(where = { "id": id })
    
    @staticmethod
    async def delete_route(id: int):
        await prisma_connection.prisma.route.delete(where = { "id": id })
        
    @staticmethod
    async def update_route(id: int, route: RouteRequestDTO):
        await prisma_connection.prisma.route.update(where = { "id": id }, data = {
            "start_location": route.start_location,
            "end_location": route.end_location,
            "price_per_km": route.price_per_km,
            "distance": route.distance,
            "date_of_execution": route.date_of_execution
        })