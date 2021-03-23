require "kemal"

module Application
    class Routes
        get "/operation/user" do |env|
            client = ReplTalk.new
            begin
                unless env.params.query.has_key?("id")
                    next client.get_user(env.params.query["name"]).to_json
                else
                    next client.get_user(env.params.query["id"].to_i).to_json
                end
            rescue err
                next {
                    "error" => "500",
                    "details" => "#{err.message}"
                }.to_json
            end
        end

        get "/operation/post" do |env|
            # ...
        end

        
    end
end