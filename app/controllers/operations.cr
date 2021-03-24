require "kemal"

module Application
    class Routes
        get "/operation/user" do |env|
            client = ReplTalk.new
            payload = env.params.query.dup

            begin
                unless payload.has_key?("id")
                    next client.get_user(payload["name"]).to_json
                else
                    next client.get_user(payload["id"].to_i).to_json
                end
            rescue err
                next {"error" => "#{err.message}"}.to_json
            end
        end

        get "/operation/posts" do |env|
            client = ReplTalk.new
            payload = env.params.query.dup

            begin
                unless payload.has_key?("searchQuery")
                    next client.get_post(payload["id"].to_i).to_json
                else
                    next client.get_posts(payload.to_h).to_json
                end
            rescue err
                next {"error" => "#{err.message}"}.to_json
            end
        end
    end
end