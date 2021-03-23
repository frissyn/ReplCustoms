require "kemal"

module Application
    class Config
        # Server configurations
        Kemal.config.port = 8080
        Kemal.config.host_binding = "0.0.0.0"
    end
end