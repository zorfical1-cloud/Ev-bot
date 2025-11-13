def format_ev_message(picks):
    if not picks:
        return "No +EV plays found right now."

    lines = ["**🔥 +EV Betting Opportunities 🔥**\n"]

    for p in picks:
        player = p["player"]
        pp = p["pp_line"]
        fd = p["fd_line"]
        ev = p["ev"]

        lines.append(
            f"**{player}**\n"
            f"• PrizePicks: `{pp}`\n"
            f"• FanDuel: `{fd}`\n"
            f"• **EV: {ev}%**\n"
        )

    return "\n".join(lines)
