from shapecms import ShapeCMS, PageView

app = ShapeCMS()


class HomeView(PageView):
    def get(self):
        return "Coming soon."


app.add_url("/", HomeView(), "test")

if __name__ == "__main__":
    app.run()
