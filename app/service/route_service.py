from app.repository.route_repository import RouteRepository
from app.repository.user_repository import UserRepository
from app.model.route import RouteRequestDTO, Route
from app.model.email import Email
from app.utils.mail_sender import MailSender
from fastapi import HTTPException, status
from app.security.authorization import session


class RouteService:
    
    @staticmethod
    async def get_all_routes():
        return await RouteRepository.get_all_routes()

    @staticmethod
    async def get_route_by_id(id: int):
        result = await RouteRepository.get_route_by_id(id)
        if result is not None:
            return result  
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No such user in database")
            

    @staticmethod
    async def create_route(data: RouteRequestDTO):
        return await RouteRepository.create_route(data)

    @staticmethod
    async def delete_route(id: int):
        return await RouteRepository.delete_route(id)

    @staticmethod
    async def update_route(id: int, data: RouteRequestDTO):
        return await RouteRepository.update_route(id, data)

    @staticmethod
    async def select_route(id: int):
        result = await RouteRepository.get_route_by_id(id)
        if result is not None and session.session_container.get('user_id') is not None:
            user = await UserRepository.get_user_by_id(session.session_container.get('user_id'))
            route_data = RouteService.__create_route_confirmation_email(result, user.email)
            await MailSender().send_selected_route_data_email(route_data)
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something bad happened. Our monkeys are working on it")
        
        
    @staticmethod
    def __create_route_confirmation_email(data: Route, user_email: str) -> Email:
        email = Email(
            email=[user_email],
            body={
                "route_id": data.id,
                "start_location": data.start_location,
                "end_location": data.end_location,
                "cost": data.price_per_km,
                "distance": data.distance,
                "date_of_execution": data.date_of_execution.strftime("%m/%d/%Y, %H:%M:%S")
            }
        )
        return email