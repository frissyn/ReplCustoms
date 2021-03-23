require "kemal"

module Application
    class Routes
        get "/" do
            render "views/index.ecr", "views/layout.ecr"
        end

        get "/user" do
            render "views/user/search.ecr", "views/layout.ecr"
        end
    end
end