package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  An SPDX version 2.X compatible verification method for software packages.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PackageVerificationCode extends IntegrityMethod {

  private List<String> packageVerificationCodeExcludedFile;
  private String hashValue;
  private String algorithm;

}