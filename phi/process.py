def reg(user, bot):
    u = " ".join(user)
    b = "".join(bot)
    f = open("data.txt","a")
    f.write("["+u+"#"+b+"]\n")
    f.close
