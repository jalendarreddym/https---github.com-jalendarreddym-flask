def get_response(user_message, data):
    if "application data for application id" in user_message.lower():
        application_id = int(user_message.split()[-1])
        application = data[data['application_id'] == application_id].to_dict('records')
        if application:
            return {'response': application[0]}
        else:
            return {'response': 'Application ID not found.'}
    else:
        return {'response': 'I can help you with application data. Please ask with "application data for application id {id}".'}
