email = SendGrid::Mail.new

email.from = SendGrid::Email.new(email: 'team@email.com')

email.subject = "App - Reset Password"

per = SendGrid::Personalization.new

per.to = SendGrid::Email.new(email: user.email, name: user.name)

per.substitutions = SendGrid::Substitution.new(key: "user_name", value: user.name.split(" ")[0].capitalize)

per.substitutions = SendGrid::Substitution.new(key: "reset_link", value: some_func(token, email: user.email))

email.personalizations = per

email.contents = Content.new(type: 'text/html', value: 'test')

email.contents = SendGrid::Content.new(type: 'text/plain', value: "Hi #{user.name}.. Click the following link to reset your password.. #{function_reset(token, email: user.email)}... This link will expire in two hours.. If you did not request your password to be reset, please ignore this email and your password will stay as it is.")

email.template_id = "6ede18bb-2eba-4958-8a57-43a58a559a0a"

response = @@sg.client.mail._('send').post(request_body: email.to_json)

puts response.status_code

puts response.body

puts response.headers
