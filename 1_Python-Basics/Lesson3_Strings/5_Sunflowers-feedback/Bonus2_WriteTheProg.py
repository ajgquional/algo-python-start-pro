feedback = 'What I liked most about Sunflowers is the caring staff'
end = len(feedback)
start = end - len('caring staff')
service = feedback[start:end]
print(service)