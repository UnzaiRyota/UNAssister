if __name__ == "__main__":
    sys.path.append("UNAssister")

    import UNAssister.Setting
    import UNAssister.CSS
    import UNAssister.UNAlpha
    
    from UNAssister.Setting import*
    from UNAssister.CSS import *
    from UNAssister.UNAlpha import *
        

reload(UNAssister.Setting)
reload(UNAssister.CSS)
reload(UNAssister.UNAlpha)

UnAlpha()
