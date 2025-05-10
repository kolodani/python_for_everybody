data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"

words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

# data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
# words = ['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']
# email = "stephen.marquard@uct.ac.za"
# pieces = ["stephen.marquard", "uct.ac.za"]
# pieces[1] = "uct.ac.za"
