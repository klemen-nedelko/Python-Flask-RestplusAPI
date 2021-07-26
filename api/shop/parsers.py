from flask_restplus import reqparse

pagination_parse = reqparse.RequestParser()
pagination_parse.add_argumnet('page', type= int, required= False, default= 1, help= 'Page number')
pagination_parse.add_argumnet('items_per_page', type= int, required= False,
                              default= 10, choices=[10,20,50], help= 'items per page')