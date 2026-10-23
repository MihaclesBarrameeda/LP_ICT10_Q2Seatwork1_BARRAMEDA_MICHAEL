from pyscript import document

def candidate_checker (e):         
    club_members = ["sage aguinaldo", "michael barrameda","andrey santos", "cyra cheang", "heather son", "miel lindaya"]

    f_name = document.getElementById('first name'). value
    l_name = document.getElementById('last name'). value
    candidate = f_name + ''+ l_name
    member_checker = candidate.lower () in club_members

    messages = (f 'Sorry {candidate}, your name is not on the list.',
    f'congragulations! {candidate} , you are now part of the social sciences club.')

    document.getElementbyId('result').inner.HTML = messages[member_checker]