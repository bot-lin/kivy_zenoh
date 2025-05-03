import zenoh

def main():
    # Open a Zenoh session
    session = zenoh.open(zenoh.Config())

    # Declare a publisher for the key "my/key"
    pub = session.declare_publisher("demo/example")

    # Publish a message to "my/key"
    pub.put("Hello, Zenoh, ZC!")

    # Close the session
    session.close()

if __name__ == "__main__":
    main()