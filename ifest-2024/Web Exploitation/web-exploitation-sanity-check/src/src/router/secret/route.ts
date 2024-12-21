import { json, Request, Response, Router } from "express";
import { safeList } from "../../utils/constant";
import CryptoJS from "crypto-js"

export const router : Router = Router()

router.use(json())

class Decryptor {
    encryptedText : string
    key: string

    constructor(encryptedText : string, key : string) {
        this.encryptedText = encryptedText;
        this.key = key
    }

    decrypt(actualPassword : string) {
        const decryptedAesText = CryptoJS.AES.decrypt(this.encryptedText, this.key).toString(CryptoJS.enc.Utf8)

        return decryptedAesText === CryptoJS.MD5(actualPassword + this.key).toString();
    }
}


router.post("/secret", (req : Request, res : Response)=>{
    try{
        const {encryptedText, id} = req.body
        const selectedSafe = safeList.filter((safe)=>safe.id === id)[0]
        const result = new Decryptor(encryptedText, selectedSafe.id).decrypt(selectedSafe.password)
        if(result){
            return res.status(200).json({location:`/secret/${selectedSafe.id}`})
        }
        return res.status(401).json({message: "Wrong password !"})
    }catch(error){
        console.log(error)
        return res.status(401).json({message: "Wrong password !"})
    }
})

router.get("/secret/:secretId", (req : Request, res: Response)=>{
    try{
        const {secretId} = req.params
        const selectedSafe = safeList.filter((safe)=>safe.id === secretId)[0]
        return res.render("secret", {safe: selectedSafe})

    }catch(error){
        console.log(error)
        return res.redirect("/")
    }
})