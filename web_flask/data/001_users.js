db.createUser(
    {
        user: "admin",
        pwd: "123",
        roles:[
            {
                role: "readWrite",
                db:   "movies_cms"
            }
        ]
    }
);