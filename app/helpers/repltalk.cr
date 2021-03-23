require "json"
require "http"

module Application
    class ReplTalk
        getter client
        getter queries
        property headers

        def initialize()
            uri = URI.parse("https://replit.com")
            @client = HTTP::Client.new(uri)
            @headers = HTTP::Headers{
                "Origin" => "https://replit.com",
                "Content-Type" => "application/json",
                "Referer" => "https://replit.com/account",
                "X-Requested-With" => "XMLHttpRequest"
            }

            @queries = {} of String => String

            Dir["#{__DIR__}/../queries/*.txt"].each do |n|
                name = n.split('/')[-1].gsub(".txt", "")
                @queries[name] = File.read(n)
            end
        end

        private def gql(name : String, op : String, vars : Hash)
            load = {
                "query" => op,
                "operationName" => name,
                "variables" => vars.to_json
            }

            res = @client.post("/graphql", @headers, form=load.to_json)
            JSON.parse(res.body)["data"].as_h
        end

        def get_user(name : String)
            gql(
                "userByUsername",
                @queries["userByName"],
                {"username" => name}
            )["user"]
        end

        def get_user(id : Int)
            gql("user", @queries["userByID"], {"user_id" => id})["user"]
        end
    end
end