db.createUser({
    user: "admin",
    pwd: "123",
    roles: [{
        role: "readWrite",
        db: "covid_ontario"
    }]
});