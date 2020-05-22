import requests

class user:
    url              = "https://intra.epitech.eu/user/?format=json"
    data             = None
    login            = None
    title            = None
    internal_email   = None
    lastname         = None
    firstname        = None
    userinfo         = None
    referent_used    = None
    picture          = None
    picture_fun	     = None
    scolaryear	     = None
    promo	         = None
    semester	     = None
    location	     = None
    documents	     = None
    userdocs	     = None
    shell	         = None
    close	         = None
    ctime	         = None
    mtime	         = None
    id_promo	     = None
    id_history	     = None
    course_code	     = None
    semester_code    = None
    school_id	     = None
    school_code	     = None
    school_title	 = None
    old_id_promo	 = None
    old_id_location	 = None
    rights	         = None
    invited	         = None
    studentyear	     = None
    admin	         = None
    editable	     = None
    restrictprofiles = None

def load(session):
    result = session.get(user.url)
    data = result.json()

    user.data             = data
    user.login            = data['login']
    user.title            = data['title']
    user.internal_email   = data['internal_email']
    user.lastname         = data['lastname']
    user.firstname        = data['firstname']
    user.userinfo         = data['userinfo']
    user.referent_used    = data['referent_used']
    user.picture          = data['picture']
    user.picture_fun      = data['picture_fun']
    user.scolaryear       = data['scolaryear']
    user.promo            = data['promo']
    user.semester         = data['semester']
    user.location         = data['location']
    user.documents        = data['documents']
    user.userdocs         = data['userdocs']
    user.shell            = data['shell']
    user.close            = data['close']
    user.ctime            = data['ctime']
    user.mtime            = data['mtime']
    user.id_promo         = data['id_promo']
    user.id_history       = data['id_history']
    user.course_code      = data['course_code']
    user.semester_code    = data['semester_code']
    user.school_id        = data['school_id']
    user.school_code      = data['school_code']
    user.school_title     = data['school_title']
    user.old_id_promo     = data['old_id_promo']
    user.old_id_location  = data['old_id_location']
    user.rights           = data['rights']
    user.invited          = data['invited']
    user.studentyear      = data['studentyear']
    user.admin            = data['admin']
    user.editable         = data['editable']
    user.restrictprofiles = data['restrictprofiles']

def search(item):
    try:
        item = user.data["%s" % item]
        return (item)
    except:
        print("Item: '%s' not found" % item)
